s = input()
s += s
n = len(s)
p = [0] * n
p[0] = 1
for i in range(1, n):
    if s[i] != s[i - 1]:
        p[i] = p[i - 1] + 1
    else:
        p[i] = 1
print(min(max(p), n // 2))
