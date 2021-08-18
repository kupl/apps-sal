n, m = list(map(int, input().split()))
a = list(sorted(map(int, input().split()), reverse=True))


def proc(n, m, a):
    possible_minimum = -1
    l, r = 1, n
    sub_c = [0] * n
    while l <= r:
        i = (l + r) // 2

        current_m = m
        for j in range(i):
            sub_c[j] = 0

        for j in range(0, n):
            pos = j % i
            if a[j] < sub_c[pos]:
                break
            current_m -= a[j] - sub_c[pos]
            sub_c[pos] += 1
            if current_m <= 0:
                break
        if current_m <= 0:
            possible_minimum = i
            r = i - 1
        else:
            l = i + 1
    return possible_minimum


print(proc(n, m, a))
