def change(a, b):
    a, b = ord(a) - 96, ord(b) - 96
    a, b = max(a, b), min(a, b)
    return min(a - b, 26 + b - a)


def mini(arr, p):
    if len(arr) == 0:
        return 0
    if arr[-1] <= p:
        return p - arr[0]
    if arr[0] >= p:
        return arr[-1] - p
    return min((arr[-1] - p), (p - arr[0])) + (arr[-1] - arr[0])


def func(s, p):
    mid = (len(s) + 1) / 2
    if p > mid:
        p = mid - (p - mid)
    mid = int(len(s) / 2)
    steps = 0
    mis = []
    for i in range(mid):
        if s[i] != s[len(s) - 1 - i]:
            steps += change(s[i], s[len(s) - 1 - i])
            mis.append(i + 1)
    steps = steps + mini(mis, p)
    return steps


l = list(map(int, input().split()))
pos = l[1]
s = input()
ans = func(s, pos)
print(int(ans))
