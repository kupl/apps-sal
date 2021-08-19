n = int(input())
v = sorted(list(map(int, input().split())))
s = [0] * n
s[0] = v[0]
for i in range(n - 1):
    s[i + 1] = (v[i + 1] + s[i]) / 2
print(s[-1])
