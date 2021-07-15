n = int(input())
a = list(map(int, input().split()))

upper = [399, 799, 1199, 1599, 1999, 2399, 2799,3199, 4800]
lower = [1, 400, 800, 1200, 1600, 2000, 2400, 2800, 3200]

cnt = 0
tops = 0
for color in range(9)[::-1]:
    for i in range(n):
        if color == 8:
            if lower[color] <= a[i] <= upper[color]:
                tops += 1
        else:
            if lower[color] <= a[i] <= upper[color]:
                cnt += 1
                break

print(max(1, cnt), cnt + tops)
