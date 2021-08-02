L, R = list(map(int, input().split()))
m = 2019

if R - L >= 2018:
    print("0")
else:
    ans = 2020
    for i in range(L, R + 1):
        for j in range(i + 1, R + 1):
            t = ((i % m) * (j % m)) % m
            ans = min(ans, t)
    print(ans)
