n, k = map(int, input().split())
a = list(map(int, input().split()))
c = [0] * 101
for i in a:
    c[i] += 1
m = (max(c) + k - 1) // k
ans = 0
for i in range(101):
    if (c[i]):
        ans += max(0, m * k - c[i])
print(ans)
