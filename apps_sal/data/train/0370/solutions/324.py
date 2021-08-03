class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        parent = {}

        def find(a):
            if a not in parent:
                parent[a] = a
                return a
            if parent[a] == a:
                return a
            parent[a] = find(parent[a])
            return parent[a]

        for num in A:
            parent[num] = num

        for num in A:
            for i in range(2, int(sqrt(num)) + 1):
                if num % i == 0:
                    parent[find(num)] = parent[find(i)]
                    parent[find(num)] = parent[find(num / i)]

        count = {}
        maxi = 1
        for num in A:
            tmp = find(num)
            if tmp not in count:
                count[tmp] = 1
            else:
                count[tmp] += 1
            maxi = max(maxi, count[tmp])

        return maxi

    def largestComponentSize2(self, A: List[int]) -> int:

        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        visited = [False] * len(A)
        group = [-1] * len(A)
        stack = []
        num = 0
        maxGrp = 0

        for i in range(len(A)):
            if visited[i] == False:
                stack.append(i)
                numGrp = 0

                while len(stack) > 0:
                    curr = stack.pop()
                    for j in range(len(A)):
                        if j == curr:
                            continue
                        if group[j] == -1:
                            if A[curr] % 2 == A[j] % 2 == 0 or gcd(A[curr], A[j]) > 1:
                                group[j] = num
                                numGrp += 1
                                stack.append(j)

                visited[i] = True
                maxGrp = max(maxGrp, numGrp)
                num += 1

        return maxGrp
