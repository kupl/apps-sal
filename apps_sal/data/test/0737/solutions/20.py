# B
n = int(input())
a = 1  # длина стороны
while a * a <= n:
    a += 1
a -= 1

p = a * 4
df = n - a * a

count = df // a
p = p + 2 * count

df -= count * a
if df > 0:
    p += 2

print(p)
