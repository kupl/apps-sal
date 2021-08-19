sm = [0] * 40000
n = int(input())
s = input()
l = len(s)
for i in range(l):
    ss = 0
    for j in range(i, l):
        ss += int(s[j])
        sm[ss] += 1
if n == 0:
    ans = 0
    for i in range(1, 40000):
        ans += sm[0] * sm[i] * 2
    ans += sm[0] * sm[0]
    print(ans)
else:
    ans = 0
    u = int(n ** 0.5)
    for i in range(1, u + 1):
        if n % i == 0:
            if n // i < 40000:
                ans += sm[i] * sm[n // i]
    ans *= 2
    if u ** 2 == n:
        ans -= sm[u] ** 2
    print(ans)
