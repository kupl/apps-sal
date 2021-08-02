import math
n, h = map(int, input().split())
lis = [list(map(int, input().split())) for _ in range(n)]

a_sort = sorted(lis, reverse=True)

b_sort = sorted(lis, key=lambda x: x[1], reverse=True)

cnt = 0
furu = a_sort[0][0]

for nage in b_sort:
    if nage[1] > furu:
        h -= nage[1]
        cnt += 1
    else:
        break

    if h <= 0:
        break

if h <= 0:
    print(cnt)
else:
    plus = int(math.ceil(h / furu))
    cnt += plus
    print(cnt)
