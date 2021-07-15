n = int(input())
k = int(input())
x = list(map(int, input().split()))
ans = 0
for i in range(n):
    if x[i] >= k - x[i]:
        ans += 2*(k - x[i])
    else:
        ans += 2*x[i]
print(ans)
