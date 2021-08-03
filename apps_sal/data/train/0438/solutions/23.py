class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        ans = -1
        l = collections.defaultdict(int)
        count = collections.defaultdict(int)
        step = 0
        for num in arr:
            step += 1
            left, right = l[num - 1], l[num + 1]
            l[num] = l[num - left] = l[num + right] = left + right + 1
            count[left + right + 1] += 1
            count[left] -= 1
            count[right] -= 1
            if count[m]:
                ans = step
        return ans
