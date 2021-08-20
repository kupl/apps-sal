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
            elif seats[i - 1] != 1:
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
            elif seats[i + 1] != 1:
                rToL[i] = rToL[i + 1] + 1
            else:
                rToL[i] = 1
        res = 1
        for i in range(len(seats)):
            if i == 0 or i == len(seats) - 1:
                if lToR[i] != -1 and rToL[i] != -1:
                    res = max(res, max(lToR[i], rToL[i]))
            elif lToR[i] != -1 and rToL[i] != -1:
                res = max(res, min(lToR[i], rToL[i]))
        return res


'\nclass Solution:\n    def maxDistToClosest(self, seats: List[int]) -> int:\n        if not seats: return 0\n        res = 0\n        que = deque()\n        que.append(-1)\n        for index, seat in enumerate(seats):\n            if seat == 1: que.append(index)\n            if len(que) == 2:\n                if que[0] == -1:\n                    res = max(res, que[1])\n                else:\n                    res = max(res, (que[1]-que[0])//2)\n                que.popleft()\n        res = max(res, len(seats)-1-que[0])\n        return res\n'
'\nclass Solution:\n    def maxDistToClosest(self, seats: List[int]) -> int:\n        res = 0\n        que = deque()\n        que.append(-1)\n        #start, end = 0, 0\n        \n        for index, seat in enumerate(seats):\n            if seat == 1: que.append(index)\n            if len(que) == 2:\n                if que[0] == -1:\n                    res = max(res, que[1])\n                else:\n                    res = max(res, (que[1]-que[0])//2)\n                que.popleft()\n                    \n        res = max(res, len(seats)-1-que[0])\n        return res\n'
