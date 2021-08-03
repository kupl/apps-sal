n, m = [int(x) for x in input().split()]
a = []
for i in range(n):
    a.append(list(input()))
b = []
for i in range(m):
    b.append(list(input()))

res = "No"

for i in range(n - m + 1):
    for j in range(n - m + 1):
        flag = True
        for k in range(m):
            for l in range(m):
                if a[k + i][l + j] != b[k][l]:
                    flag = False
        if flag:
            res = "Yes"

print(res)
