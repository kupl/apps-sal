class Solution:
    def carFleet(self, target, position, speed) -> int:
        ans, time = 0, sorted([[position[i], (target - position[i]) / speed[i]] for i in range(len(position))], reverse=True) + [[-1, float('inf')]]

        # print(time)
        for i in range(1, len(time)):
            if time[i - 1][1] < time[i][1]:
                ans += 1
            else:
                time[i][1] = time[i - 1][1]

        return ans
