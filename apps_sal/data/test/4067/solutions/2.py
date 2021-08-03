n = int(input())
x = input()
a = x.count('0')
b = x.count('1')
c = x.count('2')
s = list(c for c in x)
if a > n // 3:
    if c < n // 3:
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                s[i] = '2'
                a -= 1
                c += 1
            if c == n // 3:
                break
            if a == n // 3:
                break
    if a > n // 3:
        if b < n // 3:
            for i in range(len(s) - 1, -1, -1):
                if s[i] == '0':
                    s[i] = '1'
                    a -= 1
                    b += 1
                if b == n // 3:
                    break
                if a == n // 3:
                    break
if b > n // 3:
    if a < n // 3:
        for i in range(0, len(s),):
            if s[i] == '1':
                s[i] = '0'
                a += 1
                b -= 1
            if b == n // 3:
                break
            if a == n // 3:
                break
    if b > n // 3:
        if c < n // 3:
            for i in range(len(s) - 1, -1, -1):
                if s[i] == '1':
                    s[i] = '2'
                    b -= 1
                    c += 1
                if b == n // 3:
                    break
                if c == n // 3:
                    break
if c > n // 3:
    if a < n // 3:
        for i in range(0, len(s)):
            if s[i] == '2':
                s[i] = '0'
                a += 1
                c -= 1
            if c == n // 3:
                break
            if a == n // 3:
                break
    if c > n // 3:
        if b < n // 3:
            for i in range(0, len(s)):
                if s[i] == '2':
                    s[i] = '1'
                    b += 1
                    c -= 1
                if b == n // 3:
                    break
                if c == n // 3:
                    break
print(''.join(s))
