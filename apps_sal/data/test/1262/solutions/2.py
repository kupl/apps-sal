import heapq
import sys
input = sys.stdin.readline

n = int(input())
T = [tuple(map(int, input().split())) for i in range(n)]
C = list(map(int, input().split()))
K = list(map(int, input().split()))

H = []

for i, c in enumerate(C):
    H.append((c, i + 1))

heapq.heapify(H)

ANS = 0
USE = [0] * (n + 1)
ANS1 = []
ANS2 = []

while H:
    x = heapq.heappop(H)

    if len(x) == 2:
        cost, town = x

        if USE[town] == 1:
            continue

        ANS += cost
        USE[town] = 1
        ANS1.append(town)

        xt, yt = T[town - 1]

        for i in range(n):
            if USE[i + 1] == 1:
                continue
            costp = (abs(T[i][0] - xt) + abs(T[i][1] - yt)) * (K[i] + K[town - 1])
            if costp < C[i]:
                C[i] = costp
                heapq.heappush(H, (costp, town, i + 1))

    else:
        cost, town1, town2 = x
        if USE[town1] == 1 and USE[town2] == 1:
            continue

        ANS += cost
        USE[town2] = 1
        ANS2.append((town1, town2))

        xt, yt = T[town2 - 1]

        for i in range(n):
            if USE[i + 1] == 1:
                continue
            costp = (abs(T[i][0] - xt) + abs(T[i][1] - yt)) * (K[i] + K[town2 - 1])
            if costp < C[i]:
                C[i] = costp
                heapq.heappush(H, (costp, town2, i + 1))

sys.stdout.write(str(ANS) + "\n")
sys.stdout.write(str(len(ANS1)) + "\n")
print(*ANS1)

sys.stdout.write(str(len(ANS2)) + "\n")
for x, y in ANS2:
    sys.stdout.write(str(x) + " " + str(y) + "\n")
