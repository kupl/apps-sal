import sys
n, s = [int(x) for x in input().split()]
h1, m1 = [int(x) for x in input().split()]
if h1 * 60 + m1 >= s + 1:
    print(0, 0)
    return
for i in range(n - 1):
    h2, m2 = [int(x) for x in input().split()]
    if h2 * 60 + m2 >= h1 * 60 + m1 + 2 + s * 2:
        z = h1 * 60 + m1 + 1 + s
        print(z // 60, z % 60)
        return
    h1 = h2
    m1 = m2

z = h1 * 60 + m1 + 1 + s
print(z // 60, z % 60)
