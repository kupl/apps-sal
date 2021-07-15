n, m = map(int, input().split())
xs = list(map(int, input().split()))
ys = set(map(int, input().split()))
for i in xs:
    if i in ys:
        print(i, end = ' ')
