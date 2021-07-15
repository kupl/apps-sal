class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        # length = [0] * (len(arr) + 2)
        # cnt = [0] * (len(arr) + 1)
        # ans = -1
        # for i, a in enumerate(arr):
        #     left, right = length[a - 1], length[a + 1]
        #     length[a] = length[a - left] = length[a + right] = left + right + 1
        #     cnt[left] -= 1
        #     cnt[right] -= 1
        #     cnt[length[a]] += 1
        #     if cnt[m]:
        #         ans = i + 1
        # return ans
        
        # Union-Find
        uf = {}
        seen = [0] * (len(arr) + 1)

        def find(x):
            uf.setdefault(x, x)
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            seen[find(y)] += seen[find(x)]
            uf[find(x)] = find(y)

        ans, n = -1, len(arr)
        for i, a in enumerate(arr, 1):
            seen[a] = 1
            for b in [a - 1, a + 1]:
                if 1 <= b <= n and seen[b]:
                    if seen[find(b)] == m:
                        ans = i - 1
                    union(a, b)
        if m == n:
            ans = n
        return ans
                
                
                
                
                

