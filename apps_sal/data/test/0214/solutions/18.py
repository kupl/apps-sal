def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(mi())


ss = [input().strip(), input().strip()]
s = [a + b for a, b in zip(ss[0], ss[1])] + ['XX']
n = len(s)


def solve(i, j):
    c = 0
    k = i
    while k < j - 1:
        if s[k] == '0X' and s[k + 1] == '00':
            c += 1
            k += 2
        elif s[k] == 'X0' and s[k + 1] == '00':
            c += 1
            k += 2
        elif s[k] == '00' and s[k + 1] == 'X0':
            c += 1
            k += 2
        elif s[k] == '00' and s[k + 1] == '0X':
            c += 1
            k += 2
        elif s[k] == '00' and s[k + 1] == '00':
            c += 1
            s[k + 1] = '0X'
            k += 1
        else:
            k += 1
    return c


i = 0
c = 0
while i < n:
    if s[i] == 'XX':
        i += 1
        continue
    j = i + 1
    while s[j] != 'XX':
        j += 1
    c += solve(i, j)
    i = j
print(c)
