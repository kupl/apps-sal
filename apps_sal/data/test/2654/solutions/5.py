n = int(input())
l = []
r = []
for _ in range(n):
    (a, b) = list(map(int, input().split()))
    l.append(a)
    r.append(b)
l.sort()
r.sort()
if n % 2 == 1:
    l_mid = l[n // 2]
    r_mid = r[n // 2]
    print(r_mid - l_mid + 1)
else:
    l_mid = (l[n // 2] + l[n // 2 - 1]) / 2
    r_mid = (r[n // 2] + r[n // 2 - 1]) / 2
    print(int((r_mid - l_mid) * 2) + 1)
