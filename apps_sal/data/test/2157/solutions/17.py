n, q = list(map(int, input().split()))

a = list(map(int, input().split()))

b = [0] * (n + 1)

c = [0] * (n)

for i in range(q):

    l, r = list(map(int, input().split()))

    b[l - 1] += 1

    b[r] -= 1

cur = 0

for i in range(n):

    cur += b[i]

    c[i] = cur

c.sort()

a.sort()

cur = 0

for i in range(n):

    cur += a[i] * c[i]

print(cur)


# Made By Mostafa_Khaled
