n = int(input())
a_lst = list(map(int, input().split()))
res = []
for a in a_lst:
    tmp = a
    cnt = 0
    while tmp % 2 == 0:
        tmp = tmp // 2
        cnt += 1
    res.append(cnt)
print(min(res))
