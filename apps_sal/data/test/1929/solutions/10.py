(n, t, c) = [int(i) for i in input().split()]
h = [int(i) for i in input().split()]
res = 0
cnt = 0
for i in h:
    if i > t:
        cnt = 0
    else:
        cnt += 1
    if cnt >= c:
        res += 1
print(res)
