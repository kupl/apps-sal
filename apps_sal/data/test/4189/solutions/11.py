p = [1, 2, 5, 8, 13, 18, 25, 32, 41, 50, 61, 72, 85, 98, 113]

n = int(input())
s = h = 0

for i in range(n):
    a = input().split()[1]
    if a == 'soft':
        s += 1
    else:
        h += 1

if s > h:
    ma = s
else:
    ma = h
pp = 0
while ma > p[pp]:
    pp += 1

if s == h == p[pp] and p[pp] % 2 == 1:
    print(pp + 2)
else:
    print(pp + 1)

