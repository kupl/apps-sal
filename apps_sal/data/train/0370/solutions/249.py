class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        def find(m, a):
            while m[a] != a:
                m[a] = m[m[a]]
                a = m[a]
            return a

        def union(m, a, b):
            if m[a] == m[b]:
                return

            pa = find(m, a)
            pb = find(m, b)
            m[pa] = pb

        Max = max(A)
        m = [i for i in range(Max + 1)]
        for num in A:
            for k in range(2, int(math.sqrt(num)) + 1):
                if num % k == 0:
                    union(m, num, k)
                    union(m, num, num // k)

        count = collections.defaultdict(int)
        for num in A:
            count[find(m, num)] += 1

        return max(count.values())
