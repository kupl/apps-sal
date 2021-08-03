class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        diff = total % p
        if diff == 0:
            return 0
        modcumsum = [0]
        s = 0
        for n in nums:
            s += n
            modcumsum.append(s % p)

        d = dict()
        print(modcumsum)

        best = len(nums)
        for i in range(len(modcumsum)):
            v = modcumsum[i]
            target = (v - diff) % p

            # check if target val is in array
            if target in list(d.keys()):
                best = min(best, i - d[target])

            # add current value to the dict
            d[v] = i

        return best if best != len(nums) else -1
