n = int(input())
s = input()
res = 0
for l in range(1, n + 1):
    for beg in range(0, n - l + 1):
        hor = 0
        ver = 0
        for i in range(beg, beg + l):
            if s[i] == 'U':
                ver += 1
            if s[i] == 'D':
                ver -= 1
            if s[i] == 'R':
                hor += 1
            if s[i] == 'L':
                hor -= 1
        if hor == 0 and ver == 0:
            res += 1

print(res)
