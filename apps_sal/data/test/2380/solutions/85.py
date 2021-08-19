from collections import deque
(N, M) = map(int, input().strip().split())
A = list(map(int, input().strip().split()))
BC = [list(map(int, input().strip().split())) for _ in range(M)]
A.sort()
A = deque(A)
BC.sort(key=lambda x: x[1], reverse=True)
ans = 0
fin = False
for m in range(M):
    if fin == True:
        break
    i = 0
    while i < BC[m][0]:
        if A:
            if BC[m][1] >= A[0]:
                ans += BC[m][1]
                A.popleft()
                i += 1
            else:
                ans += sum(A)
                fin = True
                break
        else:
            fin = True
            break
if fin == False and A:
    ans += sum(A)
print(ans)
