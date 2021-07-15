class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        answer, length = 0, 0
        inds = []
        for i, num in enumerate(A):
            if num == 1:
                length += 1
            elif len(inds) < K:
                inds.append(i)
                length += 1
            elif K == 0:
                length = 0
            else:
                last_index = inds.pop(0)
                inds.append(i)
                length = (i - inds[0]) + (inds[0] - last_index)
            answer = max(answer, length)
        return answer
