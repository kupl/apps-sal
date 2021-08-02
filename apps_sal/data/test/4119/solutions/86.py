n, m = map(int, input().split())
X = sorted(set(list(map(int, input().split()))))
s = []
for i in range(m - 1):
    s.append(X[i + 1] - X[i])
s = sorted(s)[::-1]

print(sum(s[n - 1:]))
