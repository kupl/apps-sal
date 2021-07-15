n, k, p, x, y = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()

marks = []

if (n > 1):
    while (len(a) < n) and (len(a) <= (n+1)//2-2 or (n+1)//2-2 < 0 or a[(n+1)//2-2] >= y):
        a = [1] + a
        marks.append(1)
else:
    marks = [y]
    a = [y]

marks += [y] * (n - len(a))
a += [y] * (n - len(a))
a.sort()

if (sum(a) > x or a[(n+1)//2-1] < y):
    print(-1)
else:
    print(" ".join(map(str, marks)))

