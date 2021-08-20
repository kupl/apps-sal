class Solution:

    def longestOnes(self, A: List[int], K: int) -> int:
        if not A:
            return 0
        n = len(A)
        cur_max = 0
        counter = 0
        index = []
        prev = -1
        for i in range(n):
            if A[i] == 1:
                counter += 1
            elif K > 0:
                K -= 1
                counter += 1
                index.append(i)
            elif index:
                counter += 1
                temp = index.pop(0)
                counter -= temp - prev
                prev = temp
                index.append(i)
            else:
                counter = 0
            cur_max = max(cur_max, counter)
        return cur_max
