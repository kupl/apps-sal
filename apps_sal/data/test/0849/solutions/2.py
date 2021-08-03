tmp = input().split(' ')
a = []
for i in range(0, 4):
    a.append(int(tmp[i]))

p1 = a[0] / a[1]
p2 = a[2] / a[3]

tot = 10 ** 5
ans = 0.0000000000000
for i in range(0, tot):
    ans = ans + (1 - p1) ** i * (1 - p2) ** i * p1

print(ans)
