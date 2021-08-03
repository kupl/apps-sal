class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        N = len(arr) + 1

        starts = dict()
        ends = dict()

        num_groups = 0
        ans = -1

        for (step, i) in enumerate(arr):

            cur_range = [i, i]
            if i + 1 in starts:
                cur_range[1] = starts[i + 1]

                if starts[i + 1] - i == m:
                    num_groups -= 1

                del starts[i + 1]

            if i - 1 in ends:
                cur_range[0] = ends[i - 1]

                if i - ends[i - 1] == m:
                    num_groups -= 1
                del ends[i - 1]

            starts[cur_range[0]] = cur_range[1]
            ends[cur_range[1]] = cur_range[0]

            if cur_range[1] - cur_range[0] + 1 == m:
                num_groups += 1

            if num_groups > 0:
                ans = step + 1
        return ans
