def check(r, o, p):
    change = 0
    for j in range(0, a):
        if o[j] != p[j + r] and o[j] != '?':
            change += 1
    return change


a, b = input().split()
a, b = [int(a), int(b)]
s = input()
t = input()
_min = b
ans = 0
for i in range(0, b - a + 1):
    if check(i, s, t) < _min:
        _min = check(i, s, t)
        ans = i
print(_min)
for k in range(0, a):
    if s[k] != t[k + ans]:
        print(k + 1, ' ', end='')
