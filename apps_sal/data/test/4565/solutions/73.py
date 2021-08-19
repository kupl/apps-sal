n = int(input())
s = [(i == 'W') * 1 for i in list(input())]
c = [0] * (n + 1)
for i in range(n):
    c[i + 1] = c[i] + s[i]
ans = float('inf')
for i in range(n):
    t = c[i] + (n - i - 1 - c[-1] + c[i + 1])
    ans = min(ans, t)
print(ans)
