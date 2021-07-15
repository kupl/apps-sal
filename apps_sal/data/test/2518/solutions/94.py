import sys
input = sys.stdin.readline

n, a, b = list(map(int, input().split()))
R = [int(input()) for i in range(n)]

l = 0
r = 10 ** 9 + 1


# x 回で全滅できるか否か
def check(x):
    cnt = 0
    for ri in R:
        if ri - x * b > 0:
            cnt += (ri - x * b + a-b - 1) // (a-b)
    return cnt <= x

while True:
    if r - l <= 1:
        break
    mid = (l + r) // 2
    if check(mid):
        r = mid
    else:
        l = mid

if check(l):
    print(l)
else:
    print(r)

