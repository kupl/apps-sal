class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        end = {}
        n = len(arr)
        count = collections.defaultdict(int)
        string = [0] * (n + 1)
        ans = -1
        for i in range(len(arr)):
            start = arr[i]
            string[start] = 1
            left = start
            right = start
            flag1, flag2 = False, False
            if arr[i] - 1 > 0 and string[arr[i] - 1] == 1:
                l, r = end[arr[i] - 1]
                left = l
                count[r - l + 1] -= 1
                flag1 = True
            if arr[i] + 1 <= n and string[arr[i] + 1] == 1:
                l2, r2 = end[arr[i] + 1]
                right = r2
                count[r2 - l2 + 1] -= 1
                flag2 = True
            end[arr[i]] = (left, right)
            if flag1:
                end[l] = (l, right)
            if flag2:
                end[r2] = (left, r2)

            count[right - left + 1] += 1
            if count[m] > 0:
                ans = i + 1
        return ans
