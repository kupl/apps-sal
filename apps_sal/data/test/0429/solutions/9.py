s = input()
v = [i for i in s]
t = [0 for i in range(26)]
f = 0
q = 0
for i in range(len(v)):
    if v[i] == '?':
        q = q + 1
    else:
        t[ord(v[i]) - 65] += 1
    if i > 24:
        c = t.count(0)
        if c == q:
            d = []
            for k in range(26):
                if t[k] == 0:
                    d.append(chr(k + 65))
            l = 0
            for k in range(0, i - 25):
                if v[k] == '?':
                    print('A', end='')
                else:
                    print(v[k], end='')
            for k in range(i - 25, i + 1):
                if v[k] == '?':
                    print(d[l], end='')
                    l = l + 1
                else:
                    print(v[k], end='')
            for k in range(i + 1, len(v)):
                if v[k] == '?':
                    print('A', end='')
                else:
                    print(v[k], end='')
            f = 1
            break
        elif v[i - 25] == '?':
            q = q - 1
        else:
            t[ord(v[i - 25]) - 65] -= 1
if f == 0:
    print('-1')
