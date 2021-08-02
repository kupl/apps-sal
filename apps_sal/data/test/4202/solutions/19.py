L, R = list(map(int, input().split()))
l = L % 2019
r = R % 2019
if R - L >= 2019:
    ans = 0
else:
    if l < r:
        min = 100000000
        for i in range(l, r):
            for j in range(i + 1, r + 1):
                tmp = i * j % 2019
                if tmp < min:
                    min = tmp
        ans = min
    else:  # l > r:
        min = 100000000
        for i in range(l, r + 2019):
            for j in range(i + 1, r + 2019 + 1):
                tmp = i * j % 2019
                if tmp < min:
                    min = tmp
        ans = min

print(ans)
