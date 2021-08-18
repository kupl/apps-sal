n = int(input())
s = input() + "@"
t = input() + "@"
mod = 10 ** 9 + 7

b = []
for i in range(n):
    if s[i] == s[i + 1]:
        continue
    b.append(s[i] == t[i])

if b[0]:
    ans = 3
else:
    ans = 6

for i in range(1, len(b)):
    if b[i]:
        if b[i - 1]:
            ans *= 2
    else:
        if b[i - 1]:
            ans *= 2
        else:
            ans *= 3

print((ans % mod))
