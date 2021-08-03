def checkMatr(a):
    res = True
    ln = len(a)
    hln = int(ln / 2)
    if ln % 2 != 0:
        res = False
    else:
        for i in range(hln):
            if a[i] != a[ln - 1 - i]:
                res = False
    return res


n, m = list(map(int, input().split()))
table = []
for i in range(n):
    table.append(str(input()))

while checkMatr(table):
    table = table[:int(len(table) / 2)]

print(len(table))
