from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
S = input().strip()

P = (N - 11) // 2

L = deque(S)
count = 0

for j in range(P):
    while len(L) != 0 and L[0] == "8":
        L.popleft()
        count += 1

    if len(L) == 0:
        print("YES")
        return

    L.popleft()

    while len(L) != 0 and L[0] == "8":
        L.popleft()
        count += 1

if count > P:
    print("YES")
else:
    print("NO")
