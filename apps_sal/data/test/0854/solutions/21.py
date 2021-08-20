def func(n, t, a):
    count = 0
    s = sum(a)
    z = []
    if t >= s:
        count += t // s * n
        t %= s
    for i in a:
        if t >= i:
            z.append(i)
            count += 1
            t -= i
    if t >= min(a):
        count += func(len(z), t, z)
    return count


(n, t) = map(int, input().split())
a = list(map(int, input().split()))
print(func(n, t, a))
