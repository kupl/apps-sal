class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        steps = [0] * (len(arr) + 2)
        count = defaultdict(int)
        ans = -1
        for i in range(len(arr)):
            c = arr[i]
            l = c - 1
            r = c + 1
            count[steps[l]] -= 1
            count[steps[r]] -= 1
            steps[c] = steps[l - steps[l] + 1] = steps[r + steps[r] - 1] = steps[l] + steps[r] + 1
            count[steps[c]] += 1
            if count[m] > 0:
                ans = i + 1
        return ans
