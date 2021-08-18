class Solution:
    def getMaxLen(self, nums: List[int]) -> int:

        n = len(nums)
        for i in range(n):
            if nums[i] > 0:
                nums[i] = 1
            elif nums[i] < 0:
                nums[i] = -1

        ans = 0
        old = 1
        for i in range(n):
            temp = i
            count = 0
            j = i
            pro = 1
            old = 1
            while j < n:

                pro = pro * nums[j]
                if pro == 0:
                    i = j + 1
                    break

                count += 1
                if pro > 0:
                    if count > ans:
                        ans = count
                j = j + 1
                old = pro

            if pro == 0 and old > 0:
                if ans < count:
                    ans = count
            elif old < 0:

                left = 1
                right = 1
                for z in range(temp, j):
                    if nums[z] == -1:
                        break
                    left += 1
                z = j - 1
                while z >= temp:
                    if nums[z] == -1:
                        break
                    right += 1
                    z = z - 1
                q = min(left, right)
                if (j - temp + 1 - q) - 1 > ans:
                    ans = (j - temp + 1 - q) - 1
            if j >= n:
                break

        return ans
