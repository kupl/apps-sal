N = int(input())
A = list(map(int, input().split()))
count = 1
ans = 0
for i in range(N):
    a = A[i]
    if count == a:
        count += 1
    else:
        ans += 1
if ans == N:
    print(-1)
else:
    print(ans)
