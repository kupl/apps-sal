class Solution:
    def lenLongestFibSubseq1(self, A: List[int]) -> int:
        mp = {}

        for v in A:
            mp[v] = set()

        result = 0
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                a = A[i]
                b = A[j]
                l = 2
                while True:
                    if b in mp[a]:
                        break
                    if l != 2:
                        mp[a].add(b)
                    c = a + b
                    if c not in mp:
                        break
                    a, b = b, c
                    l += 1
                if l >= 3:
                    result = max(result, l)
        return result

    def lenLongestFibSubseq(self, A):
        index = {x: i for i, x in enumerate(A)}
        longest = collections.defaultdict(lambda: 2)

        ans = 0
        for k, z in enumerate(A):
            for j in range(k):
                i = index.get(z - A[j], None)
                if i is not None and i < j:
                    cand = longest[j, k] = longest[i, j] + 1
                    ans = max(ans, cand)

        return ans if ans >= 3 else 0
