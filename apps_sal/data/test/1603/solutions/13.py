def R(): return map(int, input().split())


n = int(input())
a = [0] + list(R())
s = [a, sorted(a)]
for i in range(n):
    s[0][i + 1] += s[0][i]
    s[1][i + 1] += s[1][i]
m = int(input())
print("\n".join(map(str, (s[t - 1][r] - s[t - 1][l - 1] for t, l, r in (R() for _ in range(m))))))
