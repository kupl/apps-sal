n = int(input())
ls = [int(i) for i in input().split()]
ans = []
for (i, j) in enumerate(ls):
    if j == 1:
        if i == 0:
            continue
        ans.append(ls[i - 1])
ans.append(ls[n - 1])
print(len(ans))
for i in ans:
    print(i, end=' ')
