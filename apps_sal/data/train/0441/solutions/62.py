class Solution:

    def consecutiveNumbersSum(self, num: int) -> int:
        count = 1
        queue = collections.deque()
        for i in range(1, num):
            queue.append((i, i))
        while queue:
            (cur, total) = queue.popleft()
            if total + cur + 1 == num:
                count += 1
            elif total + cur + 1 < num:
                queue.append((cur + 1, total + cur + 1))
        return count

    def consecutiveNumbersSum(self, N: int) -> int:
        count = 0
        k = 1
        while k * (k - 1) / 2 < N:
            if (N - k * (k - 1) / 2) % k == 0:
                count += 1
            k += 1
        return count
