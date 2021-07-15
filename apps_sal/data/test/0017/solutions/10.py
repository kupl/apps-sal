n, k, t = [int(i) for i in input().split()]
if t < k:
    print(t)
    return
if n + 1 <= t:
    print(n + k - t)
    return
print(k)
