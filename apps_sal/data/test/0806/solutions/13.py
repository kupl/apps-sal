(n, r, l) = (int(i) for i in input().split())
r0 = r
if r0 % 3 == 1:
    r0 += 2
elif r0 % 3 == 2:
    r0 += 1
l0 = l
if l0 % 3 == 1:
    l0 -= 1
elif l0 % 3 == 2:
    l0 -= 2
d0 = (l0 - r0) // 3 + 1
d1 = d0 - 1
d2 = d0 - 1
if r0 - r == 2:
    d1 += 1
    d2 += 1
elif r0 - r == 1:
    d2 += 1
if l - l0 == 2:
    d1 += 1
    d2 += 1
elif l - l0 == 1:
    d1 += 1
d0 = [d0]
d1 = [d1]
d2 = [d2]
for i in range(1, n):
    d0.append((d0[i - 1] * d0[0] + d1[i - 1] * d2[0] + d2[i - 1] * d1[0]) % 1000000007)
    d1.append((d0[i - 1] * d1[0] + d1[i - 1] * d0[0] + d2[i - 1] * d2[0]) % 1000000007)
    d2.append((d0[i - 1] * d2[0] + d1[i - 1] * d1[0] + d2[i - 1] * d0[0]) % 1000000007)
print(d0[n - 1])
