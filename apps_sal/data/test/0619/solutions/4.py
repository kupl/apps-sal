a, b, c = list(map(int, input().split()))

n = a // c + b // c
m1 = a % c
m2 = b % c

add = 0

if m1 + m2 >= c:
    add = c - max(m1, m2)
    n += 1

print(n, add)
