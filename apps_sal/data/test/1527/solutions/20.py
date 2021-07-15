import queue
import numpy as np

H, W = list(map(int, input().split()))
maze = [list(input()) for _ in range(H)]
dir4 = [[-1,0],[1,0],[0,-1],[0,1]]


def solveMaze(s):
    q = queue.Queue()
    q.put([s[0],s[1],0])
    times = [[999999999 for j in range(W)] for i in range(H)]
    tmpAns = 0
    times[s[0]][s[1]] = 0
    while not q.empty():
        now = q.get()
        tmpAns = max(tmpAns, now[2])
        for i in range(4):
            nextH = now[0] + int(dir4[i][0])
            nextW = now[1] + int(dir4[i][1])
            nextTime = now[2] + 1

            if nextH < 0 or nextH >= H or nextW < 0 or nextW >=W or maze[nextH][nextW] == "#" or times[nextH][nextW] <= nextTime:
                continue
            else:
                times[nextH][nextW] = nextTime
                q.put([nextH, nextW, nextTime])

    return tmpAns


ans = 0

for sH in range(H):
    for sW in range(W):
        if maze[sH][sW] == ".":
            ans = max(ans, solveMaze([sH, sW]))

print(ans)






