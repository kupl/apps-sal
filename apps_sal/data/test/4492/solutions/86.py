n, x = list(map(int, input().split()))
al = list(map(int, input().split()))

cnt = 0
for i in range(n-1):
    if al[i] + al[i+1] > x:
        if al[i+1] > (al[i] + al[i+1]) - x:
            cnt += al[i] + al[i+1] - x
            al[i+1] -= (al[i] + al[i+1] - x)
        else:
            cnt += al[i+1] + al[i] - x
            al[i+1] = 0
            al[i] = x

print(cnt)
# print(al)

