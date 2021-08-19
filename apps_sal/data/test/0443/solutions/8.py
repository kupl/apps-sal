n = int(input())
a = list(map(int, input().split()))
if n == 1:
    print(-1)
else:
    x = min(a)
    y = sum(a) - x
    if x == y:
        print(-1)
    else:
        print(1)
        print(a.index(x) + 1)
