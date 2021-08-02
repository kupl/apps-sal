from collections import deque
N = int(input())
A = list(map(int, input().split()))

B = deque([])

rev = False

for i in range(N):
    if rev:
        B.appendleft(A[i])
    else:
        B.append(A[i])
    rev ^= True

if rev:
    B = list(B)[::-1]

print((*B))
