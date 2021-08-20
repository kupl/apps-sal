(n, s) = list(map(int, input().split()))
a = [0] * n
listy = 0
for i in range(n - 1):
    (c, d) = list(map(int, input().split()))
    a[c - 1] += 1
    a[d - 1] += 1
    if a[c - 1] == 1:
        listy += 1
    if a[c - 1] == 2:
        listy -= 1
    if a[d - 1] == 1:
        listy += 1
    if a[d - 1] == 2:
        listy -= 1
if n <= 3:
    print(s)
else:
    print(float(s) * 2 / float(listy))
