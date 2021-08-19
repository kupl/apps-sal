import sys
from collections import deque
input = sys.stdin.readline


def getcnt(fromplatform, toplatform):
    return (fromplatform - toplatform) // 2


for _ in range(int(input())):
    (h, n) = list(map(int, input()[:-1].split()))
    platforms = deque(list(map(int, input()[:-1].split())))
    currenth = h
    platforms.popleft()
    platforms.append(-200)
    ans = 0
    while currenth > 2:
        if currenth - 1 == platforms[0]:
            if currenth - 2 == platforms[1]:
                platforms.popleft()
                platforms.popleft()
                currenth -= 2
            else:
                platforms.popleft()
                ans += 1
                currenth = platforms[0] + 1
        else:
            currenth = platforms[0] + 1
    print(ans)
