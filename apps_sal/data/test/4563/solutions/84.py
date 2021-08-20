n = int(input())
(t1, a1) = list(map(int, input().split()))
for i in range(n - 1):
    (t, a) = list(map(int, input().split()))
    if t1 * a == t * a1:
        pass
    elif t1 * a < t * a1:
        a1 = -(-a1 // a) * a
        t1 = a1 // a * t
    else:
        t1 = -(-t1 // t) * t
        a1 = t1 // t * a
print(a1 + t1)
