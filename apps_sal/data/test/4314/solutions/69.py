h, w = map(int, input().split())
lis = [list(input()) for i in range(h)]

fin = []
num = [0] * w

for l in lis:
    if l.count(".") != w:
        fin.append(l)
    for i in range(w):
        if l[i] == ".":
            num[i] += 1

for f in fin:
    ans = []
    for i in range(len(num)):
        if num[i] != h:
            ans.append(f[i])
    print(*ans, sep='')
