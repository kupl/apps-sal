n, a = map(int, input().split())
b = list(map(int, input().split()))
ans = [0] * n
k = a - (n - 1)

if n == 1:
    print(b[0] - 1)
    return
elif a % n == 0:
    d = a // n
    if b.count(d) == n:
        ans = [d - 1] * n
        print(*ans)
        return
s = sum(b)
for i in range(n):
    if k < b[i]:
        ans[i] += (b[i] - k)
    if (s - a) < b[i]:
        ans[i] += a - (s - b[i]) - 1

print(*ans)
