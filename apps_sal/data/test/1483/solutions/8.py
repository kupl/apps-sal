n = int(input())
ls = list(map(int, input().split()))
rls = []
for i in range(n):
    mls = [0] * n
    mls[i] += 1
    up = i
    for j in range(n):
        up = ls[up] - 1
        mls[up] += 1
        if(mls[up] == 2):
            rls.append(up + 1)
            break
print(*rls)
