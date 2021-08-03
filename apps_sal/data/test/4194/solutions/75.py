n, m = map(int, input().split())
total = sum(list(map(int, input().split())))

if n - total >= 0:
    print(n - total)
else:
    print("-1")
