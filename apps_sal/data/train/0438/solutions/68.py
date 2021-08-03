class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        lens = defaultdict(int)  # len of union, count

        unions = {}  # start:end, or vice versa

        latest = -1

        for step, i in enumerate(arr):
            start = unions.pop(i - 1, i)
            end = unions.pop(i + 1, i)

            unions[start] = end
            unions[end] = start

            left_size = i - start
            right_size = end - i

            lens[left_size] -= 1
            lens[right_size] -= 1
            lens[left_size + right_size + 1] += 1

            if lens[m]:
                latest = step + 1

        return latest

        # 1 0 1 0 1
