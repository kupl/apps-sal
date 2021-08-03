class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        parent = {}

        for num in A:
            parent[num] = num

        def find(a):
            if a not in parent:
                parent[a] = a
                return a
            if parent[a] == a:
                return a
            parent[a] = find(parent[a])
            return parent[a]

        for num in A:
            for i in range(2, int(sqrt(num)) + 1):
                if num % i == 0:
                    parent[find(num)] = parent[find(i)]
                    parent[find(num)] = parent[find(num / i)]

        count = defaultdict(int)
        maxi = 1
        for num in A:
            tmp = find(num)
            count[tmp] += 1
            maxi = max(maxi, count[tmp])

        return maxi
