from numpy import cumsum
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
sa = cumsum(a)
sb = cumsum(b)
ans = 0
for i in range(n):
    ans = max(ans, sa[i] + sb[n-1] - sb[i] + b[i])

print(ans)

