from collections import deque
N = int(input())
A = [int(i) for i in input().split()]
A.sort(reverse=True)
q = deque()
for i in range(N):
    q.append(A[i])
s = []
w = True
while q:
    if len(q) == 1:
        break
    else:
        i = q.popleft()
        j = q.popleft()
        if i == j:
            s.append(i)
        else:
            q.appendleft(j)
        if len(s) == 2:
            print(s[0] * s[1])
            w = False
            break
if w:
    print(0)
