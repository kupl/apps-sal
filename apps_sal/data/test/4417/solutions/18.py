q = int(input())
for y in range(q):
    (n, k) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    (mn, mx) = (min(a), max(a))
    if k * 2 < mx - mn:
        print(-1)
    else:
        print(mn + k)
