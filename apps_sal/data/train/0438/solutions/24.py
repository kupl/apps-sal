class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        forward = [0] * len(arr)
        backward = [0] * len(arr)
        counter = collections.defaultdict(int)
        res = -1
        step = 1
        for i in arr:
            i = i - 1
            if i - 1 >= 0 and i + 1 < len(arr):
                curr = forward[i - 1] + 1 + backward[i + 1]
                counter[forward[i - 1]] -= 1
                if counter[forward[i - 1]] == 0:
                    del counter[forward[i - 1]]
                counter[backward[i + 1]] -= 1
                if counter[backward[i + 1]] == 0:
                    del counter[backward[i + 1]]
                backward[i - forward[i - 1]] = curr
                forward[i + backward[i + 1]] = curr
                counter[curr] += 1
            elif i == 0 and i + 1 == len(arr):
                if m == 1:
                    return step
                else:
                    break
            elif i == 0:
                curr = 1 + backward[i + 1]
                counter[backward[i + 1]] -= 1
                if counter[backward[i + 1]] == 0:
                    del counter[backward[i + 1]]
                backward[i] = curr
                forward[i + backward[i + 1]] = curr
                counter[curr] += 1
            else:
                curr = forward[i - 1] + 1
                counter[forward[i - 1]] -= 1
                if counter[forward[i - 1]] == 0:
                    del counter[forward[i - 1]]
                forward[i] = curr
                backward[i - forward[i - 1]] = curr
                counter[curr] += 1
            if counter[m] >= 1:
                res = step
            step += 1
        return res
