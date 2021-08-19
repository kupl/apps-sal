s = input()
k = int(input())
ls = len(s)
res = []
for i in range(1, k + 1):
    for j in range(ls - i + 1):
        res.append(s[j:j + i])
ress = sorted(list(set(res)))
print(ress[k - 1])
