class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        last_step = -1
        n = len(arr)
        left, right = [0] * n, [0] * n
        tmp_arr = [0] * n
        memo = collections.defaultdict(lambda: 0)
        for i, num in enumerate(arr):
            tmp_arr[num - 1] = 1
            left[num - 1] = 1 + (left[num - 2] if num >= 2 else 0)
            right[num - 1] = 1 + (right[num] if num < n else 0)

            if num >= 2 and tmp_arr[num - 2]:
                memo[left[num - 2] + right[num - 2] - 1] -= 1
                right[num - 2] += right[num - 1]
                if (num - 1 - (left[num - 1] - 1)) != (num - 2):
                    right[num - 1 - (left[num - 1] - 1)] += right[num - 1]

            if num < n and tmp_arr[num]:
                memo[left[num] + right[num] - 1] -= 1
                left[num] += left[num - 1]
                # print(\"haha\", tmp_arr, left, right)
                if (num - 2 + right[num - 1]) != num:
                    left[num - 2 + right[num - 1]] += left[num - 1]

            memo[left[num - 1] + right[num - 1] - 1] += 1

            if memo[m] > 0:

                last_step = i + 1
            # print(memo, tmp_arr, left, right)
        return last_step
