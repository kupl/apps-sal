from collections import deque
K =int(input())

INF = 10**9+7
A = [INF] * (K)

q = deque()
q.append(1)
A[1] = 1
while q:
    x = q.popleft()
    if A[(x*10)%K] > A[x]:
        A[(x*10)%K] = A[x]
        q.appendleft((x*10)%K)
    if A[(x+1)%K] > A[x]+1:
        A[(x+1)%K] = A[x]+1
        q.append((x+1)%K)

print(A[0])
