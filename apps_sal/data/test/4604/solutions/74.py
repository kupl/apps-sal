n = int(input())
a = list(map(int, input().split()))
mod = 10 ** 9 + 7
if n % 2 == 0:
    b = [2 if i % 2 == 1 else 0 for i in range(n)]
else:
    b = [2 if i % 2 == 0 else 0 for i in range(n)]
    b[0] = 1
c = [0 for i in range(n)]
for i in range(n):
    c[a[i]] += 1
if b != c:
    print(0)
else:
    ans = 1
    for i in range(n // 2):
        ans *= 2
        ans %= mod
    print(ans)
