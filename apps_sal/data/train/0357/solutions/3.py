class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        lToR = [0 for _ in range(len(seats))]
        rToL = [0 for _ in range(len(seats))]
        for i in range(len(seats)):
            if seats[i] == 1:
                lToR[i] = -1
                continue
            if i == 0:
                if seats[i] == 0:
                    lToR[i] = 1
            else:
                if seats[i - 1] != 1:
                    lToR[i] = lToR[i - 1] + 1
                else:
                    lToR[i] = 1
        for i in range(len(seats) - 1, -1, -1):
            if seats[i] == 1:
                rToL[i] = -1
                continue
            if i == len(seats) - 1:
                if seats[i] == 0:
                    rToL[i] = 1
            else:
                if seats[i + 1] != 1:
                    rToL[i] = rToL[i + 1] + 1
                else:
                    rToL[i] = 1
        res = 1
        for i in range(len(seats)):
            if i == 0 or i == len(seats) - 1:
                if lToR[i] != -1 and rToL[i] != -1:
                    res = max(res, max(lToR[i], rToL[i]))
            else:
                if lToR[i] != -1 and rToL[i] != -1:
                    res = max(res, min(lToR[i], rToL[i]))
        return res


'''
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        if not seats: return 0
        res = 0
        que = deque()
        que.append(-1)
        for index, seat in enumerate(seats):
            if seat == 1: que.append(index)
            if len(que) == 2:
                if que[0] == -1:
                    res = max(res, que[1])
                else:
                    res = max(res, (que[1]-que[0])//2)
                que.popleft()
        res = max(res, len(seats)-1-que[0])
        return res
'''


'''
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        res = 0
        que = deque()
        que.append(-1)
        
        for index, seat in enumerate(seats):
            if seat == 1: que.append(index)
            if len(que) == 2:
                if que[0] == -1:
                    res = max(res, que[1])
                else:
                    res = max(res, (que[1]-que[0])//2)
                que.popleft()
                    
        res = max(res, len(seats)-1-que[0])
        return res
'''
