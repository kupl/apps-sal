class Solution:

    def minSubarray(self, nums: List[int], p: int) -> int:
        s = sum(nums)
        if s < p:
            return -1
        rem = s % p
        if rem == 0:
            return 0
        (r, cur, l) = (dict({(0, -1)}), 0, len(nums))
        ret = l
        for i in range(l):
            cur = (cur + nums[i]) % p
            print(cur)
            if cur - rem in r:
                ret = min(ret, i - r[cur - rem])
            if cur + p - rem in r:
                ret = min(ret, i - r[cur + p - rem])
            r[cur] = i
        return -1 if ret == l else ret
