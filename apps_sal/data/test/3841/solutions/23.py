p, k = map(int, input().split())
a = []
while p != 0:
    t = p % k
    a.append(t)
    p = -((p - t) // k)
print(len(a))
a = list(map(str, a))
print(' '.join(a))
