from collections import deque
N = int(input())
A = list(map(int, input().split()))

B = deque([])

rev = False

for i in range(N):
    if not rev:
        B.append(A[i])
    else:
        B.appendleft(A[i])
    rev ^= True

if rev:
    B = list(B)[::-1]

print((*B))
