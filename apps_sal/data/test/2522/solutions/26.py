import heapq
from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


CA = Counter(A)
CB = Counter(B)

H = []

for ca in CA:
    if CA[ca] > 0 and CB[ca] > 0:
        if CA[ca] + CB[ca] > N:
            print("No")
            return
        H.append((-(CA[ca] + CB[ca]), ca))

heapq.heapify(H)

ANSDICT = dict()

while len(H) >= 2:
    c1, x1 = heapq.heappop(H)
    c1 = -c1

    c2, x2 = heapq.heappop(H)
    c2 = -c2

    if x1 in ANSDICT:
        ANSDICT[x1].append(x2)
    else:
        ANSDICT[x1] = [x2]

    if x2 in ANSDICT:
        ANSDICT[x2].append(x1)
    else:
        ANSDICT[x2] = [x1]

    CA[x1] -= 1
    CA[x2] -= 1
    CB[x1] -= 1
    CB[x2] -= 1

    if CA[x1] > 0 and CB[x1] > 0:
        heapq.heappush(H, (-(c1 - 2), x1))

    if CA[x2] > 0 and CB[x2] > 0:
        heapq.heappush(H, (-(c2 - 2), x2))

ANS = [-1] * N

for i in range(N):
    a = A[i]
    if a in ANSDICT and len(ANSDICT[a]) != 0:

        x = ANSDICT[a].pop()
        ANS[i] = x

if H:
    cc, xx = H[0]
    cc = -cc

    for i in range(N):
        if ANS[i] == -1 and A[i] != xx:
            ANS[i] = xx
            CB[xx] -= 1

            if CB[xx] == 0:
                break

ind = 0
for cb in CB:
    while CB[cb] != 0:
        while ANS[ind] != -1:
            ind += 1
        ANS[ind] = cb
        CB[cb] -= 1

print("Yes")
print((*ANS))
