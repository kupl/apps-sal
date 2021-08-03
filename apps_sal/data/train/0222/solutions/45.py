class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        S = set(A)
        i = 0
        max_len = 0
        while i < len(A) - 1:
            j = i + 1
            while j < len(A):
                subSeq = [A[i], A[j]]
                while subSeq[-1] + subSeq[-2] in S:
                    subSeq.append(subSeq[-1] + subSeq[-2])
                    # print(subSeq)
                    if len(subSeq) > max_len:
                        max_len = len(subSeq)
                j += 1
            i += 1
        return max_len
