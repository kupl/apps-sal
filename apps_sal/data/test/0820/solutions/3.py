n = int(input())
m = int(input())
p = []
for i in range(n):
    k = int(input())
    p.append(k)
p.sort()
col = 0
pos = n - 1
while m > 0:
    m -= p[pos]
    pos -= 1
    col += 1
print(col)
