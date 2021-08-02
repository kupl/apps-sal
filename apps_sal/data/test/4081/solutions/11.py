n = int(input())
i = 0
j = n - 1
cur = 0
ls = list(map(int, input().split()))
res = []
while i <= j:
    if ls[i] > cur and ls[j] > cur:
        if ls[i] < ls[j]:
            res.append('L')
            cur = ls[i]
            i += 1
        else:
            res.append('R')
            cur = ls[j]
            j -= 1
    elif ls[i] > cur:
        res.append('L')
        cur = ls[i]
        i += 1
    elif ls[j] > cur:
        res.append('R')
        cur = ls[j]
        j -= 1
    else:
        break
print(len(res))
for i in res:
    print(i, end='')
print()
