class Solution:
    def minTaps(self, n: int, minjump: List[int]) -> int:

        for i in range(n + 1):
            left = max(0, i - minjump[i])
            right = min(n, i + minjump[i])
            minjump[left] = max(minjump[left], right - left)
        # print(minjump)
        jump = 1
        steps = minjump[0]
        maxreach = minjump[0]
        lastindex, maxjump = 0, minjump[0]
        for i in range(1, n + 1):
            steps -= 1
            if steps < 0:
                return -1

            if i + minjump[i] > maxreach:
                maxreach = minjump[i] + i
                maxjump = minjump[i]
                lastindex = i
            if steps == 0 and i != n:
                steps = lastindex + maxjump - i
                jump += 1
        return jump
