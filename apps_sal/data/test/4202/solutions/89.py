(l, r) = map(int, input().split())
ans = 2018
if r - l >= 2019:
    print('0')
else:
    for i in range(l, r):
        for j in range(i + 1, r + 1):
            temp = i * j % 2019
            ans = min(ans, temp)
    print(ans)
