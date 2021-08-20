(n, m, k) = map(int, input().split())
A = [0] * m
for i in range(m):
    A[i] = list(map(int, input().split()))
if k != 0:
    ans = set(list(map(int, input().split())))
if k == 0 or k == n:
    print(-1)
else:
    per = float('infinity')
    for i in range(m):
        if A[i][0] in ans and A[i][1] not in ans or (A[i][0] not in ans and A[i][1] in ans):
            per = min(per, A[i][2])
    if per != float('infinity'):
        print(per)
    else:
        print(-1)
