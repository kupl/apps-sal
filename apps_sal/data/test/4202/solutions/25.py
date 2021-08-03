l, r = list(map(int, input().split()))
if r - l >= 2019:
    print((0))
    return
ans = 2018
for i in range(l, r):
    for j in range(i + 1, r + 1):
        if ans > i * j % 2019:
            ans = i * j % 2019
print(ans)
