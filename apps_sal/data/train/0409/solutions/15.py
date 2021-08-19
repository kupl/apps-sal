class Solution:

    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        mod = 1000000007
        (fms, sms, msf, meh) = (0, 0, 0, 0)
        for i in range(3):
            for num in arr:
                meh = max(0, meh + num)
                msf = max(msf, meh)
            if i == 0:
                fms = msf
            elif i == 1:
                sms = msf
        diff = msf - sms
        print(fms, sms, msf, diff)
        return (sms + diff * (k - 2)) % 1000000007
