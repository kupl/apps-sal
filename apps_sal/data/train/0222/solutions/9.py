class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        longest = 0
        ss = set(A)
        for (i, x) in enumerate(A):
            for (j, y) in enumerate(A[i + 1:]):
                tmp = x + y
                if tmp in ss:
                    counter = 2
                    t = x
                    while True:
                        if t + y in ss:
                            (t, y) = (y, t + y)
                            counter += 1
                        else:
                            break
                    if longest < counter:
                        longest = counter
        return longest
