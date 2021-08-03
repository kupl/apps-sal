class Solution:
    def racecar(self, target: int) -> int:

        targetLen = len(bin(target)) - 2
        barrier = (1 << targetLen)
        # print(tar6021getLen, barrier)
        stack = [(0, target)]
        dp = {target: 0}

        while stack:
            # print(stack)
            step0, dist = heapq.heappop(stack)

            for i in range(targetLen + 1):
                move = (1 << i) - 1
                step1 = step0 + i
                if move != dist:
                    step1 += 1
                newDist = -(dist - move)
                if abs(newDist) <= barrier and (newDist not in dp or dp[newDist] > step1):
                    heapq.heappush(stack, (step1, newDist))
                    dp[newDist] = step1

        return dp[0]


#         stack = [(0, 0, 1)]
#         visited = {(0,1):0}

#         while stack:
#             stepNow, loc, speed = heapq.heappop(stack)
#             if visited[(loc, speed)] < stepNow:
#                 continue

#             loc1 = loc+speed
#             speed1 = speed*2
#             if loc1 == target:
#                 return stepNow + 1
#             if (loc1, speed1) not in visited or visited[(loc1, speed1)] > stepNow+1:
#                 visited[(loc1, speed1)] = stepNow + 1
#                 heapq.heappush(stack, (stepNow +1, loc1, speed1))


#             loc1 = loc
#             speed1 = -1 if speed > 0 else 1
#             if (loc1, speed1) not in visited or visited[(loc1, speed1)] > stepNow+1:
#                 visited[(loc1, speed1)] = stepNow + 1
#                 heapq.heappush(stack, (stepNow +1, loc1, speed1))
