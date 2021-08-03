from sys import stdin, stdout
import math

n, k = map(int, stdin.readline().split())
values = list(map(int, stdin.readline().split()))
ans = sum(values)
cnt = 0


def round(v):
    if math.ceil(v) - v <= 1 / 2:
        return math.ceil(v)
    else:
        return math.floor(v)


while round(ans / n) < k:
    ans += k
    n += 1
    cnt += 1


stdout.write(str(cnt))
