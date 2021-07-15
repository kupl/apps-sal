n, m = [int(i) for i in input().split()]
list_a = [[s for s in input().split()] for i in range(0, n)]
list_ans = [str(s) for s in range(1, m + 1)]
for i in range(0, n):
    for j in range(0, m):
        if list_ans[j] not in list_a[i][1:]:
            list_ans[j] = '0'
print(len([s for s in list_ans if s != '0']))
