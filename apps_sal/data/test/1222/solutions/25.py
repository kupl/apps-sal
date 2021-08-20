K = int(input())
cand = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
for i in range(9):
    tmp = []
    for val in cand[-1]:
        if str(val)[-1] != '0':
            tmp.append(val * 10 + int(str(val)[-1]) - 1)
        tmp.append(val * 10 + int(str(val)[-1]))
        if str(val)[-1] != '9':
            tmp.append(val * 10 + int(str(val)[-1]) + 1)
    cand.append(tmp)
ans = []
for l in cand:
    for i in l:
        ans.append(i)
ans.sort()
print(ans[K - 1])
