z = []
m = 0
s = 0
for _ in range(int(input())):
    a = list(map(int, input().split()))
    z += [[max(a[1:]), a[0]]]
    if z[-1][0] > m:
        m = z[-1][0]
for i in z:
    s += (m - i[0]) * i[1]
print(s)
