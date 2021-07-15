import bisect

n = int(input())
x = list(map(int, input().split()))
q = int(input())

x.sort()

x0 = min(x)
x1 = max(x)

for i in range(q):
    m = int(input())
    if m < x0:
        print(0)
    elif m > x1:
        print(n)
    else:
        print(bisect.bisect_left(x, m+1))

