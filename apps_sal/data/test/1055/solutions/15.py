def f(a):
    if a == sorted(a):
        return len(a)
    else:
        k = len(a) // 2
        if len(a) % 2 == 0:
            return max(f(a[:k]), f(a[k:]))
        else:
            return max(f(a[:k]), f(a[k:]), f(a[k + 1:]), f(a[k + 1:]))


n, a = int(input()), list(map(int, input().split()))
print(f(a))
