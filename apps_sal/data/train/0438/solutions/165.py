class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        def helper(start, end, curStep):
            if curStep == 1:
                return curStep if m == 1 else -1

            if end - start + 1 < m:
                return -1

            elif end - start + 1 == m:
                return curStep

            else:
                idx = arr[curStep - 1]

                if idx < start or idx > end:
                    return helper(start, end, curStep - 1)

                else:
                    return max(helper(start, idx - 1, curStep - 1), helper(idx + 1, end, curStep - 1))

        return helper(1, len(arr), len(arr))
