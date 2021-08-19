class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1
        eV = max(bloomDay)
        sV = min(bloomDay)
        while sV <= eV:
            mV = (sV + eV) // 2
            i = 0
            x = 0
            c = 0
            while i < n:
                if bloomDay[i] <= mV:
                    x += 1
                    if x >= k:
                        c += 1
                        if c >= m:
                            break
                        x = 0
                else:
                    x = 0
                i += 1
            else:
                sV = mV + 1
                continue
            eV = mV - 1
        return sV
