a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
ans = 0
e = 0
for i in range(a[0]):
    d = list(map(int, input().split()))
    c .append(d)
for i in c:
    for j in range(a[1]):
        e += b[j] * i[j]

    if e + a[2] > 0:
        ans += 1
    e = 0
print(ans)
