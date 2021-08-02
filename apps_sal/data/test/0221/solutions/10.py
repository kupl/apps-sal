
n, k = map(int, input().split())

if n <= 2 * k + 1:
    print(1)
    print(n // 2 + 1)
    return

l = 2 * (k + 1)
r = 2 * (2 * k + 1)
cnt = 0
while not (l <= n <= r):
    cnt += 1
    l += 2 * k + 1
    r += 2 * k + 1

print(cnt + 2)

m = n - cnt * (2 * k + 1)
a = m // 2
ans = [a - k - 1]
r = ans[0] + k

while r < n - 1:
    if r + k + 1 < n:
        ans.append(r + k + 1)
    r = ans[-1] + k

for i in ans:
    print(i + 1, end=' ')
print()
