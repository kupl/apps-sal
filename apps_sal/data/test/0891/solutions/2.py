(n, m) = [int(x) for x in input().split()]
s = input()


def lefti(i):
    return (n + i - 1) % n


def left(i):
    return s[lefti(i)]


def righti(i):
    return (i + 1) % n


def right(i):
    return s[righti(i)]


def inverse(c):
    return 'B' if c == 'W' else 'W'


res = [' ' for i in range(n)]
for i in range(n):
    cr = s[i]
    pr = left(i)
    nx = right(i)
    if cr == pr or cr == nx:
        res[i] = cr
all_empty = False
i = 0
while res[i] == ' ':
    i += 1
    if i >= n:
        all_empty = True
        break
if all_empty:
    for k in range(n):
        res[k] = s[k] if m % 2 == 0 else inverse(s[k])
else:
    krug = i
    i = righti(i)
    while i != krug:
        while res[i] != ' ' and i != krug:
            i = righti(i)
        if i == krug:
            break
        l = lefti(i)
        while res[i] == ' ':
            i = righti(i)
        r = i
        real_l = l
        for j in range(m):
            res[righti(l)] = res[l]
            res[lefti(r)] = res[r]
            l = righti(l)
            r = lefti(r)
            if righti(l) == r or l == r:
                break
    for k in range(n):
        if res[k] == ' ':
            res[k] = s[k] if m % 2 == 0 else inverse(s[k])
print(''.join(res))
