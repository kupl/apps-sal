n = int(input())
a = list(map(int, input().split()))
newa = []
for i in range(n):
    newa.append(a[i] - i - 1)
newa.sort()
if n % 2 == 0:
    mid = (newa[n // 2 - 1] + newa[n // 2]) // 2
else:
    mid = newa[n // 2]
ans = 0
for i in range(n):
    ans += abs(newa[i] - mid)
print(ans)
