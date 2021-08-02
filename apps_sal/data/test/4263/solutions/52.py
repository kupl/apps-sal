s = list(input())
n = len(s)
res = 0
for i in range(n):
    for j in range(i, n):
        temp = s[i:j + 1]
        if all(i in 'ATGC' for i in temp):
            res = max(res, len(temp))
print(res)
