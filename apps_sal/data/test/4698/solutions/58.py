n = int(input())
tl = list(map(int, input().split()))
m = int(input())
pxl = [list(map(int, input().split())) for _ in range(m)]
s = sum(tl)
for (p, x) in pxl:
    print(s - tl[p - 1] + x)
