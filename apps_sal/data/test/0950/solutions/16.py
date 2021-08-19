def ri():
    return list(map(int, input().split()))


digit = '0123456789'
letter = 'abcdefghijklmnopqrstuvwxyz'
sym = '#*&'
val = [[] for _ in range(3)]
val[0] = digit
val[1] = letter
val[2] = sym
(n, m) = ri()
minm = [[10000000000 for _ in range(3)] for __ in range(n)]
for ln in range(n):
    line = input()
    for i in range(3):
        for mov in range(m):
            if line[mov] in val[i] or line[-mov] in val[i]:
                minm[ln][i] = mov
                break
ans = 10 ** 10
for i1 in range(n):
    for i2 in range(n):
        for i3 in range(n):
            if i1 != i2 and i1 != i3 and (i2 != i3):
                ans = min(ans, minm[i1][0] + minm[i2][1] + minm[i3][2])
print(ans)
