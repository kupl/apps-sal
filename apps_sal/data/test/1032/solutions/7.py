import sys
lines = sys.stdin.readlines()
(n, p) = map(int, lines[0].strip().split(' '))
arr = list(map(int, lines[1].strip().split(' ')))
arr.sort()
counter = {}
for a in arr:
    if a not in counter:
        counter[a] = 0
    counter[a] += 1
lower = max(arr[-1] - n + 1, 1)
(a, b, c, d) = (lower - 1, -1, -1, arr[-1] + 1)


def check(val):
    pt = 0
    cnt = 0
    while pt < n and arr[pt] <= val:
        cnt += 1
        pt += 1
    if cnt >= p:
        return 1
    while cnt > 0:
        val += 1
        cnt -= 1
        if val in counter:
            cnt += counter[val]
        if cnt >= p:
            return 1
        if val >= arr[-1]:
            break
    if cnt <= 0 or val < arr[-1]:
        return -1
    else:
        return 0


exist = False
while a < d - 1:
    mid = (a + d) // 2
    res = check(mid)
    if res == 1:
        d = mid
    elif res == -1:
        a = mid
    else:
        exist = True
        break
if exist:
    b = mid
    c = mid
    while a < b - 1:
        mid = (a + b) // 2
        res = check(mid)
        if res == 0:
            b = mid
        else:
            a = mid
    while c < d - 1:
        mid = (c + d) // 2
        if check(mid) == 1:
            d = mid
        else:
            c = mid
if exist:
    print(c - b + 1)
    print(' '.join(map(str, range(b, c + 1))))
else:
    print(0)
    print()
