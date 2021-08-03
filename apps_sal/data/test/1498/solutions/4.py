import sys

input = sys.stdin.readline

server, task = list(map(int, input().split()))
serverstatus = [0] * server

for i in range(task):
    moment, serven, time = list(map(int, input().split()))
    ava = 0
    total = 0

    d = serverstatus[:]

    for i in range(server):
        if ava < serven and serverstatus[i] <= moment:
            ava += 1
            total += i + 1

            d[i] = moment + time
        elif ava == serven:
            break

    if ava < serven:
        print(-1)
    else:
        print(total)

        serverstatus = d[:]
