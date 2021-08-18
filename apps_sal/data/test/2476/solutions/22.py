from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))

lst = [0] * (N + 1)
for a in A:
    lst[a - 1] += 1
lst.sort()

s = [0] * (N + 1)
for i in range(N):
    s[i + 1] = s[i] + lst[i + 1]


def check(x, k):
    i = bisect_left(lst, x) - 1
    total = x * (N - i) + s[i]
    return total >= x * k


for k in range(1, N + 1):
    l = 0
    r = N // k + 1
    while l + 1 < r:
        c = (l + r) // 2
        if check(c, k):
            l = c
        else:
            r = c
    print(l)
