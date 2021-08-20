from math import ceil
t = int(input())
for test in range(t):
    (l, r) = list(map(int, input().split()))
    odd = 0
    st = 2 * ceil(l / 2)
    end = 2 * (r // 2)
    even = (st + end) * ((end - st) // 2 + 1) // 2
    st = 2 * (l // 2) + 1
    end = 2 * ceil(r / 2) - 1
    odd = (st + end) * ((end - st) // 2 + 1) // 2
    print(int(even - odd))
