N, K = list(map(int, input().split()))

point = []
for _ in range(N):
    point.append(list(map(int, input().split())))

point.sort(key=lambda x: x[0])

shin = 10**200
able = N - K
for i in range(able + 1):
    temp_high = point[:N - i]
    for j in range(able + 1 - i):
        temp_low = temp_high[j:]
        for k in range(able + 1 - i - j):
            temp_left = temp_low[:]
            temp_left.sort(key=lambda x: x[1])
            temp_left = temp_left[k:len(temp_left) - (able + 1 - i - j) + k + 1]
            if temp_left:
                ans = temp_left[:]
            elif temp_low:
                ans = temp_low[:]
            else:
                ans = temp_high[:]
            x = []
            y = []
            for item in ans:
                x.append(item[0])
                y.append(item[1])
            num = ((max(x) - min(x)) * (max(y) - min(y)))
            shin = min(shin, num)

print(shin)
