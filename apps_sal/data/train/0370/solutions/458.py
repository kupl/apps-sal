class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313]
        graph = defaultdict(list)
        divs = defaultdict(list)
        for i in A:
            n = i
            for k in primes:
                if k > n:
                    break
                if n % k == 0:
                    graph[k].append(i)
                    divs[i].append(k)
                    while n % k == 0:
                        n = n // k
            if n > 1:
                graph[n].append(i)
                divs[i].append(n)
        nodes = {i: 0 for i in A}
        seen = set()
        cnt = 1

        def dfs(node):
            nodes[node] = cnt
            for div in divs[node]:
                if div not in seen:
                    seen.add(div)
                    for each in graph[div]:
                        if nodes[each] == 0:
                            dfs(each)
        for i in A:
            if nodes[i] == 0:
                dfs(i)
                cnt += 1
        return max(Counter(nodes.values()).values())
