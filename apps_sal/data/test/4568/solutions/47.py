n = int(input())
s = input()

cnt = 0
for i in range(1, n - 1):
    tmp = 0
    r, l = s[:i], s[i:]
    rs = list(set(r))
    for ri in rs:
        if l.count(ri) > 0:
            tmp += 1
    cnt = max(cnt, tmp)

print(cnt)
