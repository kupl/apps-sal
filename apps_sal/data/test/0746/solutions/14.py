[a, b] = map(int, input().split(" "))
n = int(input())

min_time = -1


def get_time(a, b, x, y, v):
    return ((y - b)**2 + (x - a)**2)**0.5 / v


for i in range(n):
    [x, y, v] = map(int, input().split(" "))
    t = get_time(a, b, x, y, v)
    if min_time == -1 or t < min_time:
        min_time = t

print(min_time)
