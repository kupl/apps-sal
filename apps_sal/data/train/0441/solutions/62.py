class Solution:
    # Backtrack
    def consecutiveNumbersSum(self, num: int) -> int:
        count = 1

        queue = collections.deque()
        for i in range(1, num):
            queue.append((i, i))  # cur, sum

        while queue:
            cur, total = queue.popleft()
            # add the next number
            if total + cur + 1 == num:
                count += 1
            elif total + cur + 1 < num:
                queue.append((cur + 1, total + cur + 1))
        return count
    
    # N = (x + 0) + (x + 2) + ... + (x + k - 1)
    # N = x * k + (k - 1) * k / 2 -> N - (k - 1) * k / 2 = x * k.
    # So as long as N - (k - 1) * k / 2 is x times of k, there is a solution.
    # Iterate all possible values of k in the rage [1, k * (k - 1) / 2 < N]
    def consecutiveNumbersSum(self, N: int) -> int:
        count = 0
        k = 1
        while k * (k - 1) / 2 < N:
            if (N - k * (k - 1) / 2) % k == 0:
                count += 1
            k += 1
        return count

