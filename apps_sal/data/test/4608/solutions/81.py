import sys
N = int(input())
d = [int(input()) for i in range(N)]

cnt = 0
button = d[0]
while button != 2:
    button = d[button - 1]
    cnt += 1

    if cnt > 100000:
        print(-1)
        return

print(cnt + 1)
