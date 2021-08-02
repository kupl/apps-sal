n, t = map(int, input().split())
s = "0" + input()
f = s.find('.')
if f == -1:
    print(s[1:])
    return
r = list(s[:f] + s[f + 1:])
for i in range(f, len(r)):
    if r[i] >= "5" and r[i] <= "9":
        while r[i] >= "5" and r[i] <= "9":
            if i < f or t <= 0:
                break
            i -= 1
            z = ord(r[i]) + 1
            while z == ord("9") + 1:
                i -= 1
                z = ord(r[i]) + 1
            # print(r[i])
            while len(r) != i + 1:
                r.pop()
            r[-1] = chr(z)
            t -= 1
        break
if r[0] == '0':
    r = r[1:]
    f -= 1
r += ['0'] * max(f - len(r), 0)
if len(r) == f:
    print(*r, sep='')
else:
    print(*r[:f], '.', *r[f:], sep='')
