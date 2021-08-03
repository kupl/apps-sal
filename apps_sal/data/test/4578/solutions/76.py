n, x = input().split(" ")
n = int(n)
x = int(x)

d = 0
m = []

for i in range(n):
    m.append(int(input()))
m.sort()

for i in range(n):
    if(x >= m[i]):
        d += 1
        x -= m[i]

if x > m[0]:
    res = int(x / m[0])
    d += res
print(d)
