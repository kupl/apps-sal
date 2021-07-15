n, x, y = map(int, input().split())
ar = list(map(int, input().split()))
if x > y:
    print(n)
else:
    num = 1
    for i in ar:
        if i <= x:
            num += 1
    print(num // 2)
