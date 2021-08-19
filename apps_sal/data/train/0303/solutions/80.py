class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        opt = [arr[0]]
        for i in range(1, len(arr)):
            opt.append(0)
            subseqLenMax = min(k, i + 1)
            for subseqLen in range(1, subseqLenMax + 1):
                subseqSum = subseqLen * max(arr[i - subseqLen + 1:i + 1])
                if subseqLen < i + 1:
                    prevOpt = opt[i - subseqLen]
                else:
                    prevOpt = 0
                optTemp = prevOpt + subseqSum
                if optTemp > opt[i]:
                    opt[i] = optTemp
        return opt[len(opt) - 1]
