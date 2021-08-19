class Solution:

    def maxEqualFreq(self, nums: List[int]) -> int:
        freqs = defaultdict(int)
        freqfreq = defaultdict(int)
        rec = 0
        for (i, n) in enumerate(nums):
            freqs[n] += 1
            freqfreq[freqs[n]] += 1
            if freqs[n] != 1:
                freqfreq[freqs[n] - 1] -= 1
                if freqfreq[freqs[n] - 1] == 0:
                    del freqfreq[freqs[n] - 1]
            if len(freqfreq) < 3:
                if len(freqfreq) == 1 and len(freqs) == 1:
                    rec = i + 1
                elif len(freqfreq) == 1 and list(freqfreq.keys())[0] == 1:
                    rec = i + 1
                elif len(freqfreq) == 2:
                    fs = sorted(freqfreq.keys())
                    if fs[0] == 1 and freqfreq[fs[0]] == 1:
                        rec = i + 1
                    elif fs[0] + 1 == fs[1] and freqfreq[fs[1]] == 1:
                        rec = i + 1
        return rec
