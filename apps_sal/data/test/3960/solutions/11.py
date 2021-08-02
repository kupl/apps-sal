n = int(input())

a = list(map(int, input().split()))

da, p = [], 1

for i in range(n - 1):

    da.append(p * abs(a[i] - a[i + 1])); p *= -1

m1, m2, s1, s2 = 0, 0, 0, 0

for x in da:

    s1 += x

    if s1 < 0: s1 = 0

    s2 -= x

    if s2 < 0: s2 = 0

    m1 = max(m1, s1); m2 = max(m2, s2)

print(max(m1, m2))


# Made By Mostafa_Khaled
