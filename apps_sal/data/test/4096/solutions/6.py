(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))


def proc(n, m, a):
    a = list(sorted(a, reverse=True))
    for i in range(1, n + 1):
        sub_m = [0] * i
        sub_c = [0] * i
        for j in range(n):
            pos = j % i
            sub_m[pos] += max(0, a[j] - sub_c[pos])
            sub_c[pos] += 1
        if sum(sub_m) >= m:
            return i
    return -1


print(proc(n, m, a))
