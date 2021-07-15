from collections import deque
h, w = map(int, input().split())
mine = [[] for _ in range(h+2)]
mine[0] = deque(["." for _ in range(w+2)])
mine[-1] = deque(["." for _ in range(w+2)])
for i in range(h):
    mine[i+1] = deque(list(input()))
    mine[i+1].append(".")
    mine[i+1].appendleft(".")
for i in range(1, h+1):
    for j in range(1, w+1):
        if mine[i][j] == "#":
            print("#", end="")
        else:
            counter = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if (k or l) and mine[i+k][j+l] == "#":
                        counter += 1
            print(counter, end="")
    print()
