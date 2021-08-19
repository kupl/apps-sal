class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        opt = [arr[0]]
        for i in range(1, len(arr)):

            opt.append(0)  # At index i

            subseqLenMax = min(k, i + 1)  # To avoid counting past index 0

            # For the length of each possible subsequence which includes (and ends at) index i:
            for subseqLen in range(1, subseqLenMax + 1):

                # Find the max possible sum of the subsequence
                subseqSum = subseqLen * max(arr[i - subseqLen + 1: i + 1])

                # Add to the optimal solution from before
                if subseqLen < i + 1:
                    prevOpt = opt[i - subseqLen]
                else:  # Entire arr
                    prevOpt = 0
                optTemp = prevOpt + subseqSum

                # print('for opt', i, ' sublen =', subseqLen, '   subseqSum = ',subseqSum, ' optTemp = ', optTemp)

                # Compare to the other possible subsequence sums
                if optTemp > opt[i]:
                    opt[i] = optTemp

            # print(opt)

        return opt[len(opt) - 1]
