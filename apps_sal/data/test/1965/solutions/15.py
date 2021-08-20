q = int(input())
for _ in range(q):
    (n, x) = map(int, input().split())
    l = list(map(int, input().split()))
    g = l.count(x)
    dup = sum(l)
    if g == 0:
        if dup == x * n:
            print(1)
        else:
            print(2)
    elif l == [x] * n:
        print(0)
    else:
        print(1)
