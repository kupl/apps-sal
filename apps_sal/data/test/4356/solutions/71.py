n, m = map(int, input().split())
a = [input() for i in range(n)]
b = [input() for j in range(m)]
res = "No"

if m == 1:
    for i in a:
        if b[0] in i:
            res = "Yes"
else:
    for k in range(n - m + 1):
        if b[0] in a[k]:
            for l in range(n - m + 1):
                if b[0] == a[k][l:m + l]:
                    cnt = 0
                    for o in range(m - 1):
                        if b[o + 1] == a[k + o + 1][l:m + l]:
                            cnt += 1
                    if cnt == m - 1:
                        res = "Yes"

print(res)
