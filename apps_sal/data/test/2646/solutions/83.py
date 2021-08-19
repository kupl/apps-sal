from collections import deque
N, M = map(int, input().split())
A = [0] * M
B = [0] * M
C = [[] for i in range(N + 1)]

for i in range(M):
    A[i], B[i] = sorted(list(map(int, input().split())))
    C[A[i]].append(B[i])
    C[B[i]].append(A[i])

d = [-1] * (N + 1)
d[0] = 0
d[1] = 0

queue = deque([1])
while queue:
    now = queue.popleft()
    for i in C[now]:
        if d[i] != -1:
            continue
        if d[i] == -1:
            d[i] = now
#    d[i]=d[now]+1
        queue.append(i)
# print(d)
# return
# E=[0]*(N+1)
# for i in range(M):
#  if d[B[i]]-d[A[i]]==1 and E[B[i]]==0:E[B[i]]=A[i]
#  elif d[A[i]]-d[B[i]]==1 and E[A[i]]==0:E[A[i]]=B[i]
if d.count(0) > 2:
    print('No')
    exit
print('Yes')
for i in range(2, N + 1):
    print(d[i])
