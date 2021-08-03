a = input()
b = input()
c = 0
for i in range(1, len(b)):
    if b[i] != b[i - 1]:
        c += 1
s = 0
for i in range(len(b)):
    if a[i] != b[i]:
        s += 1
ans = int(s & 1 == 0)
for i in range(len(a) - len(b)):
    s += c
    if a[i] != b[0]:
        s += 1
    if a[i + len(b)] != b[-1]:
        s += 1
    ans += int(s & 1 == 0)
print(ans)
