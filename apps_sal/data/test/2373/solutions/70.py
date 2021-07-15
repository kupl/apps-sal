import math

n = int(input())
p = [x- 1 for x in map(int, input().split())]

cnt, flag = 0, 0
ans = 0
for i in range(n):
    if p[i] == i and flag:
        cnt += 1
    elif p[i] == i:
        cnt += 1
        flag = 1
    elif p[i] != i and flag:
        if cnt == 1:
            ans += 1
        else:
            ans += math.ceil(cnt/2)

        cnt, flag = 0, 0
if flag:
    if cnt == 1:
        ans += 1
    else:
        ans += math.ceil(cnt/2)

print(ans)
