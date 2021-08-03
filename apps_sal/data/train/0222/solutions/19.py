class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:

        longest = 0

        ss = set(A)
        for i, x in enumerate(A):
            for j, y in enumerate(A[i + 1:]):
                tmp = x + y
                if(tmp in ss):
                    ret = [x, y]
                    t = x
                    while(True):
                        if(t + y in ss):
                            t, y = y, t + y
                            ret.append(y)
                        else:
                            break
                    if(longest < len(ret)):
                        longest = len(ret)
        return longest
