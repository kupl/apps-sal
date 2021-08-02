L, R = list(map(int, input().split()))
ans = 2020
if R - L >= 4037:
    print((0))
else:
    for i in range(L, R):
        for j in range(i + 1, R + 1):
            temp = ((i % 2019) * (j % 2019)) % 2019
            if ans > temp:
                ans = temp
    print(ans)
