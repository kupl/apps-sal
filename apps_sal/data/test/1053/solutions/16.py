L = input().split()
n = int(L[0])
n -= 1
k = 0
while (1 << k) < n:
    k += 1
ans = 0
for i in range(0, k + 1):
    ans += (1 << i) * ((n + (1 << (i + 1)) - (1 << i)) // (1 << (i + 1)))
print(ans)
