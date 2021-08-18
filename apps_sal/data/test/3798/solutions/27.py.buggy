def f(b, n):
    if n < b:
        return n
    else:
        return f(b, n // b) + n % b


n = int(input())
s = int(input())
if n == s:
    print(n + 1)
    return

for i in range(2, int(n**0.5) + 3):
    if f(i, n) == s:
        print(i)
        return

ans = 10**13
for k in range(1, int(n**0.5) + 3):
    if (n - s) % k != 0 or n - s < 0:
        continue
    b = (n - s) // k + 1
    if b == 1:
        continue
    if f(b, n) == s:
        ans = min(b, ans)

if ans != 10**13:
    print(ans)
else:
    print(-1)
