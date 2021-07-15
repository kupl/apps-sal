R = lambda:map(int, input().split())
n = int(input())
v = list(R())
s = [[0] * (n + 1)]
for i in range(n):
  s[0][i + 1] = s[0][i] + v[i]
v = sorted(v)
s += [[0] * (n + 1)]
for i in range(n):
  s[1][i + 1] = s[1][i] + v[i]
m = int(input())
print("\n".join(map(str, (s[t - 1][r] - s[t - 1][l - 1] for t, l, r in (R() for _ in range(m))))))
