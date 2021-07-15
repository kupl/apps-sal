from collections import deque
class Solution:
    # def racecar(self, target: int) -> int:
    #     # position, speed
    #     queue = deque([(0,1)])
    #     nsteps = -1
    #     while queue:
    #         levelSize = len(queue)
    #         nsteps += 1
    #         for _ in range(levelSize):
    #             pos, speed = queue.popleft()
    #             if pos == target:
    #                 return nsteps
    #             # Always consider moving the car in the direction it is already going
    #             queue.append( (pos+speed, speed*2) )
    #             # Only consider changing the direction of the car if one of the following conditions is true
    #             if (pos>target and speed>0) or \\
    #                (pos<target and speed<0) or \\
    #                (pos+speed>target and speed>0) or \\
    #                (pos+speed<target and speed<0):
    #                 queue.append( (pos, -1 if speed>0 else 1) )
    #     return nsteps
    def __init__(self):
        self.dp = {0: 0}
    def racecar(self, t: int) -> int:
        if t in self.dp:
            return self.dp[t]

        n = t.bit_length()
        if 2**n - 1 == t:
            self.dp[t] = n
        else:
            # go pass the target, stop and turn back
            self.dp[t] = self.racecar(2**n-1-t) + n + 1
            # Go as far as possible before pass target, stop and turn back
            for m in range(n-1):
                self.dp[t] = min(self.dp[t], self.racecar(t - 2**(n-1) + 1 + 2**m - 1) + (n - 1) + m + 2)
        return self.dp[t]

