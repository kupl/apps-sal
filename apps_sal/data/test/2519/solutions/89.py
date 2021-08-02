n, k = map(int, input().split())
p = list(map(int, input().split()))

s = 0
acsum = [0]
for x in p:
    s += (x + 1) / 2
    acsum.append(s)

ans = -1
for i in range(n - k + 1):
    ans = max(ans, acsum[i + k] - acsum[i])
print(ans)
