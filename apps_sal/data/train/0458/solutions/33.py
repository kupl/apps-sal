class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        acc = []
        for num in nums:
            if len(acc) == 0:
                acc.append(num % p)
                pass
            else:
                acc.append((num + acc[-1]) % p)
                pass
            pass

        if acc[-1] % p == 0:
            return 0
        orig = acc[-1] % p
        d = {}
        ret = len(nums)
        for i in range(len(acc)):
            num = acc[i]
            find = (p + num - orig) % p
            if find in d:
                ret = min(ret, i - d[find])
                pass
            if num == orig:
                ret = min(ret, i + 1)
                pass
            d[num] = i
            pass

        return ret if ret != len(nums) else -1
