s = input().split()
n = int(s[0])
m = int(s[1])
x = int(s[2])
y = int(s[3])

city_a = []
city_b = []

v = input().split()
w = input().split()

for i in range(n):
    city_a.append(int(v[i]))
for i in range(m):
    city_b.append(int(w[i]))

city_a.sort()
city_b.sort()

p = city_a.pop()
q = city_b[0]

check = False

for i in range(x + 1, y+1):
    if p < i <= q:
        check = True
        break

if check:
    print('No War')
else:
    print('War')

