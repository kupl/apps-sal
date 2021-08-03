t, s, q = [int(x) for x in input().split()]
a = 0
while s < t:
    s = s * q
    a = a + 1
print(a)
