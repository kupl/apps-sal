# cook your dish here
n = int(input())
a = list(map(int, input().split()))

cnt, max_till = 0, 0
res = []
for i in a:

    if i == 0:
        res.append(cnt)
        cnt = 0

    else:
        cnt += 1

res.append(cnt)
print(max(res))
