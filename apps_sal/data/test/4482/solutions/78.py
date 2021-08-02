N = int(input())
a = list(map(int, input().split()))
b = 0
for i in range(N):
    b += a[i]
r = round(b / N)
ans = 0
for i in range(N):
    ans += (a[i] - r)**2
print(ans)
