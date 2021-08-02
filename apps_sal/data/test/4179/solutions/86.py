n, m, c = list(map(int, input().split()))
b = list(map(int, input().split()))
a = []
d = 0
for i in range(n):
    a.append(list(map(int, input().split())))
    combined1 = [x * y for (x, y) in zip(a[i], b)]
    if sum(combined1) + c > 0:
        d += 1

print(d)
