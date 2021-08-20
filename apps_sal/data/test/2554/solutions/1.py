def max_sub(a):
    total_max = 0
    cur_max = 0
    for v in a:
        cur_max += v
        cur_max = max(cur_max, 0)
        total_max = max(total_max, cur_max)
    return total_max


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a1 = list(a[::2])
    a2 = list(a[1::2])
    d1 = list((y - x for (x, y) in zip(a1, a2)))
    d2 = list((y - x for (x, y) in zip(a1[1:], a2)))
    print(sum(a1) + max(max_sub(d1), max_sub(d2)))
