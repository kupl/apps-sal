(n, m) = list(map(int, input().split()))
b = True
nach = 0
con = 0
nn = 0
cc = 0
for i in range(n):
    s = input()
    c = s.count('*')
    bb = True
    for j in range(m):
        if bb:
            if s[j] == '*':
                bb = False
                if b:
                    nn = j
                else:
                    nn = min(nn, j)
        if s[j] == '*':
            cc = max(cc, j)
    if b:
        if c != 0:
            b = False
            nach = i
            con = i
    if c != 0:
        con = i
m1 = cc - nn + 1
m2 = con - nach + 1
print(max(m1, m2))
