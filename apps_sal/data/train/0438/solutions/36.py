class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        bits = [0] * (len(arr) + 2)
        answ = -1
        num_groups = 0
        for step, idx in enumerate(arr):
            before = bits[idx - 1]
            after = bits[idx + 1]
            group = 1
            if before + after == 0:
                bits[idx] = 1
            elif before == 0:
                bits[idx] = after + 1
                bits[idx + 1] = 0
                bits[idx + after] = after + 1
                group = after + 1
            elif after == 0:
                bits[idx] = before + 1
                bits[idx - 1] = 0
                bits[idx - before] = before + 1
                group = before + 1
            else:
                bits[idx - 1], bits[idx + 1] = 0, 0
                bits[idx - before], bits[idx + after] = before + after + 1, before + after + 1
                group = before + after + 1

            if group == m:
                num_groups += 1
            if before == m:
                num_groups -= 1
            if after == m:
                num_groups -= 1

            if num_groups > 0:
                answ = step + 1

        return answ
