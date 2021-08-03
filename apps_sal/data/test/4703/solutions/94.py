import itertools
s = input()
n = len(s) - 1
ans = 0
for v in itertools.product(["+", ""], repeat=n):
    x = s[0]
    for i in range(n):
        x += v[i] + s[i + 1]
    ans += eval(x)
print(ans)
