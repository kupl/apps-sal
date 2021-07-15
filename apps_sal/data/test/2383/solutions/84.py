N = int(input())
A = list(map(int, input().split()))

cnt = 0
idx = 1
for i, a in enumerate(A):
    if idx == a:
        idx += 1
    else:
        cnt += 1

if cnt == N:
    print(-1)
else:
    print(cnt)
