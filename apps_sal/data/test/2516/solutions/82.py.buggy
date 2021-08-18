n, p = [int(_) for _ in input().split()]
s = input()

if p == 2 or p == 5:
    ans = 0
    for i in range(n):
        if int(s[i]) % p == 0:
            ans += i + 1
    print(ans)
    return

t = [0 for i in range(n + 1)]
P = [0 for i in range(p)]
P[0] += 1
d = 1
for i in range(1, n + 1):
    t[i] = (t[i - 1] + int(s[n - i]) * d) % p
    P[t[i]] += 1
    d = d * 10 % p
ans = 0
for c in P:
    ans += c * (c - 1) // 2
# print(t)
print(ans)
