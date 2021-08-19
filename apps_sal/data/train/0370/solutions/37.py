from collections import defaultdict


class UnionFind:
    def __init__(self, length):
        self.parent = list(range(length))
        self.size = [1] * length

    def find(self, i):
        if self.parent[i] == i:
            return i
        if self.parent[i] != i:
            return self.find(self.parent[i])

    # A utility function to do union of two subsets
    def union(self, x, y):
        x_set, y_set = self.find(x), self.find(y)
        if x_set == y_set:
            return
        self.parent[x_set] = y_set
        self.size[y_set] += self.size[x_set]
        self.size[x_set] = 0


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        # brute force is look at each node and see if we can connect it to every other node
        # after we are done connecting, we check every node and see keep track of longest path

        if len(A) <= 0:
            return 0

        '''# key: node value
        # values: list of connected components
        nodes = defaultdict(list)
        
        gcf_cache = {}
        def greatest_common_factor(a, b):
            if (a,b) in gcf_cache:
                return gcf_cache[(a,b)]
            
            if (b,a) in gcf_cache:
                return gcf_cache[(b,a)]
            
            # euclidean algo
            # Everything divides 0  
            if (a == 0): 
                return b 
            if (b == 0): 
                return a 

            # base case 
            if (a == b): 
                return a 

            # a is greater 
            if (a > b): 
                gcf = greatest_common_factor(a-b, b)
                gcf_cache[(a,b)] = gcf
                gcf_cache[(b,a)] = gcf
                return gcf
            gcf = gcd(a, b-a)
            gcf_cache[(a,b)] = gcf
            gcf_cache[(b,a)] = gcf
            return gcf
        
        def dfs(node):
            visited = set()
            stack = [(node,0)]
            max_path = -float('inf')
            while(stack):
                current_node, current_path = stack.pop()
                if current_node:
                    visited.add(current_node)
                    current_path += 1
                    max_path = max(max_path, current_path)
                    neighbors = nodes[current_node]

                    for i in range(len(neighbors)):
                        if neighbors[i] not in visited:
                            stack.append((neighbors[i], current_path))
            return max_path
        
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                gcf = greatest_common_factor(A[i], A[j])
                if gcf > 1:
                    nodes[A[i]].append(A[j])
                    nodes[A[j]].append(A[i])
        
        result = 1
        for i in nodes.keys():
            path = dfs(i)
            print(path)
            result = max(result, dfs(i))
        return result'''

        # try union find
        # reference: https://leetcode.com/problems/largest-component-size-by-common-factor/discuss/200643/Python-1112-ms-beats-100-Union-Find-and-Prime-factor-decomposition-with-Optimization
        def primeFactors(n):
            out = set()
            while n % 2 == 0:
                out.add(2)
                n //= 2
            for i in range(3, int(math.sqrt(n)) + 1, 2):
                while n % i == 0:
                    out.add(i)
                    n //= i
            if n > 2:
                out.add(n)
            return out

        uf = UnionFind(len(A))

        primeToIndex = {}
        for i, a in enumerate(A):
            primes = primeFactors(a)
            for p in primes:
                if p in primeToIndex:
                    uf.union(i, primeToIndex[p])
                primeToIndex[p] = i
        return max(uf.size)
