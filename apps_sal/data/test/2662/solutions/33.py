import bisect
n = int(input())
a = [int(input()) for i in range(n)][::-1]

color_num = [a[0]]
for i in range(1, n):
    if a[i] >= color_num[-1]:
        color_num.append(a[i])
    else:
        temp = bisect.bisect_right(color_num, a[i])
        color_num[temp] = a[i]


print(len(color_num))
