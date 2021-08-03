from math import atan2, pi

n = int(input())

a = [list(map(int, input().split())) for i in range(n)]

a = sorted(atan2(y, x) for x, y in a)

d = [a[i + 1] - a[i] for i in range(n - 1)]

d.append(2 * pi - a[n - 1] + a[0])

print(360 - 180 * max(d) / pi)


# Made By Mostafa_Khaled
