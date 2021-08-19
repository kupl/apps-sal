SS = []
a = int(input())
for i in range(a):
    (k, n, a, b) = map(int, input().split())
    k -= n * b
    if k > 0:
        ll = k // (a - b)
        if k % (a - b) == 0:
            ll -= 1
        SS.append(min(ll, n))
    else:
        SS.append(-1)
for s in SS:
    print(s)
