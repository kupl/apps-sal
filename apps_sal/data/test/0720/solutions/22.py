n = int(input())
a = []
b = []
for i in range(n):
    (A, B) = list(map(int, input().split()))
    a.append(A)
    b.append(B)
count = 1
sa = 0
sb = 0
for i in range(n):
    if sa != sb:
        if min(a[i], b[i]) >= max(sa, sb):
            ma = max(sa, sb)
            sa = ma
            sb = ma
            count += 1
        else:
            sa = a[i]
            sb = b[i]
            continue
    count += min(a[i], b[i]) - sa
    sa = a[i]
    sb = b[i]
print(count)
