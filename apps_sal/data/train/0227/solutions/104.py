class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        count = 0
        max_count = 0

        buf = K
        l = r = 0
        needs_buf = False
        while l < len(A) and r < len(A):
            if A[r] == 1:
                count += 1
                r += 1
            elif A[r] == 0:
                if buf:
                    buf -= 1
                    count += 1
                    r += 1
                else:
                    needs_buf = True

            if needs_buf:
                if A[l] == 0:
                    buf += 1
                    needs_buf = False
                count -= 1
                l += 1

            if count > max_count:
                max_count = count
            # print(A[l:r])

        # print(f'l: {l}, r: {r}')
        return max_count
