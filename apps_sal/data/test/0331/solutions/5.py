n, m, k = list(map(int, input().split()))
a = list(map(int, input().split()))
r = 10000
for i in range(n):
    if a[i] <= k and a[i] != 0:
        r = min(r, abs(m-i-1))
print(r*10)

