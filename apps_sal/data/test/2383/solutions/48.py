N = int(input())
a = [int(i) for i in input().split()]
ans = 0
l = 1
for i in range(N):
    if l == a[i]:
        l += 1
    else:
        ans += 1
if ans == N:
    print(-1)
else:
    print(ans)
