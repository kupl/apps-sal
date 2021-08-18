
n, m = map(int, input().split())
point_s = 0
point_e = n + 1

if n % 2 == 0:
    for i in range(1, m + 1):
        point_s += 1
        point_e -= 1
        print("{} {}".format(point_s, point_e))
        if n % 4 == 0 and (point_e - point_s - 1) * 2 == n:
            point_e -= 1
        elif n % 4 != 0 and (point_e - point_s - 1) * 2 == n + 2:
            point_e -= 1
elif n % 2 == 1:
    for i in range(1, m + 1):
        point_s += 1
        point_e -= 1
        print("{} {}".format(point_s, point_e))
