class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        comps = [0 for _ in range(len(arr) + 2)]
        size = collections.defaultdict(int)
        ans = -1
        for i, n in enumerate(arr):
            left, right = comps[n - 1], comps[n + 1]
            comps[n - left] = comps[n + right] = comps[n] = left + right + 1
            # print(comps)
            
            size[comps[n]] += 1
            size[left] -= 1
            size[right] -= 1
            if size[m] > 0:
                ans = i + 1
        return ans

