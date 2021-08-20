class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        neg = [0 for ii in range(len(nums))]
        zero = []
        if nums[0] < 0:
            neg[0] = 1
        elif nums[0] == 0:
            zero.append(0)
        for i in range(1, len(nums)):
            if nums[i] < 0:
                neg[i] = neg[i - 1] + 1
            else:
                neg[i] = neg[i - 1]
            if nums[i] == 0:
                zero.append(i)
        l = 0
        ans = 0
        if len(zero) == 0:
            if neg[len(nums) - 1] % 2 == 0:
                ans = max(ans, len(nums))
            else:
                (first, last) = (-1, -1)
                for i in range(len(nums)):
                    if nums[i] < 0:
                        last = i
                        if first == -1:
                            first = i
                ans = max(ans, last)
                ans = max(ans, len(nums) - first - 1)
        for z in zero:
            if z == l:
                l = z + 1
                continue
            else:
                if l == 0:
                    if neg[z - 1] % 2 == 0:
                        ans = max(ans, z)
                    else:
                        (first, last) = (-1, -1)
                        for i in range(l, z):
                            if nums[i] < 0:
                                last = i
                                if first == -1:
                                    first = i
                        ans = max(ans, last)
                        ans = max(ans, z - first - 1)
                elif (neg[z - 1] - neg[l - 1]) % 2 == 0:
                    ans = max(ans, z - l)
                else:
                    (first, last) = (-1, -1)
                    for i in range(l, z):
                        if nums[i] < 0:
                            last = i
                            if first == -1:
                                first = i
                    ans = max(ans, last - l)
                    ans = max(ans, z - first - 1)
                l = z + 1
        z = len(nums)
        if l == 0:
            if neg[z - 1] % 2 == 0:
                ans = max(ans, z)
            else:
                (first, last) = (-1, -1)
                for i in range(l, z):
                    if nums[i] < 0:
                        last = i
                        if first == -1:
                            first = i
                ans = max(ans, last)
                ans = max(ans, z - first - 1)
        elif (neg[z - 1] - neg[l - 1]) % 2 == 0:
            ans = max(ans, z - l)
        else:
            (first, last) = (-1, -1)
            for i in range(l, z):
                if nums[i] < 0:
                    last = i
                    if first == -1:
                        first = i
            ans = max(ans, last - l)
            ans = max(ans, z - first - 1)
        return ans
