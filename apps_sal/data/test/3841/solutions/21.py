(n, k) = map(int, input().split())
a = []
while n != 0:
    t = n % k
    a.append(t)
    n = -((n - t) // k)
print(len(a))
a = list(map(str, a))
print(' '.join(a))
