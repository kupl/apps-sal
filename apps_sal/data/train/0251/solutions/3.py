class Solution:

    def clumsy(self, N: int) -> int:
        count = 1
        ans = [N]
        for i in range(N - 1, 0, -1):
            if count % 4 == 1:
                ans[-1] *= i
            elif count % 4 == 2:
                ans[-1] = int(ans[-1] / i)
            elif count % 4 == 3:
                ans.append(i)
            else:
                ans.append(-i)
            count += 1
        return sum(ans)
