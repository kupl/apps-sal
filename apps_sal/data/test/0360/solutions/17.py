n = int(input())
A = [list(map(int, input().split())) for i in range(n)]
k = int(input())
ans = 0
for i in range(n):
    l, r = A[i]
    if k <= r:
        ans += 1
print(ans)
