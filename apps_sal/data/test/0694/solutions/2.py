# zdelano dobrim chelovekom vnizy :D
s, x, pfx = input(), 0, []
a, b = list(map(int, input().split()))
try:
    for i, c in enumerate(s, 1):
        x = (x * 10 + int(c)) % a

        if not x and s[i] != '0':
            pfx.append(i)
except IndexError:
    pass
x, p, i = 0, 1, len(s)
for stop in reversed(pfx):
    for i in range(i - 1, stop - 1, -1):
        x = (x + (int(s[i])) * p) % b
        p = p * 10 % b
    if not x:
        print("YES")
        print(s[:i])
        print(s[i:])
        return
print("NO")
