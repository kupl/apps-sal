from collections import deque
N,M = map(int,input().split())
A = list(map(int,input().split()))
bc = [tuple(map(int,input().split())) for _ in range(M)]
for x in A:
    bc.append((1,x))
bc.sort(key=lambda x:x[1], reverse=True)
A = []
for b,c in bc:
    while len(A) < N and b > 0:
        b -= 1
        A.append(c)
    if len(A) == N:
        break
A.sort(reverse=True)
print(sum(A))
