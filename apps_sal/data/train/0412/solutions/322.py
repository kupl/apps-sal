class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        current_sums = {}
        current_sums[0] = 1
        new_sums = {}
        out = 0
        for die in range(1, d + 1):
            for face in range(1, f + 1):
                for summ in list(current_sums.keys()):
                    curr = summ + face
                    if curr == target and die == d:
                        out += current_sums[summ]
                    elif curr < target:
                        if curr in list(new_sums.keys()):
                            new_sums[curr] += current_sums[summ]
                        else:
                            new_sums[curr] = current_sums[summ]
            current_sums = new_sums
            new_sums = {}
        return out % (10 ** 9 + 7)
