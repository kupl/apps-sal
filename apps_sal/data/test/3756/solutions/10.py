def R():
    return map(int, input().split())


(n, t) = R()
s = list(input())
r = -1
l = s.index('.') + 1
for i in range(l, n):
    if s[i] >= '5':
        r = i
        break
for i in range(r, max(l - 1, r - t), -1):
    if s[i] >= '5':
        if i - 1 != l - 1:
            s[i - 1] = str((int(s[i - 1]) + 1) % 10)
            r = i - 1
        else:
            s[i - 2] = str((int(s[i - 2]) + 1) % 10)
            r = l - 2
            if s[r] == '0':
                for j in range(r - 1, -1, -1):
                    if s[j] == '9':
                        s[j] = '0'
                    else:
                        s[j] = str((int(s[j]) + 1) % 10)
                        break
                if s[0] == '0':
                    s = ['1'] + s
                    r += 1
print(''.join(s[:r + 1]) if r >= 0 else ''.join(s))
