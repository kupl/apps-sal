class Solution:

    def minSumOfLengths(self, arr, target):
        result = inf = 2 ** 31 - 1
        i = window = count = 0
        preMin = deque([(-1, inf)])
        for (j, num) in enumerate(arr):
            window += num
            while window > target:
                window -= arr[i]
                i += 1
            while len(preMin) >= 2 and preMin[1][0] <= i - 1:
                preMin.popleft()
            if window == target:
                curr = j - i + 1
                n = preMin[0][1]
                if result > curr + n:
                    result = curr + n
                if curr < preMin[-1][-1]:
                    preMin.append((j, curr))
                if curr == 1:
                    count += 1
                if count == 2:
                    return 2
        return result if result < inf else -1
