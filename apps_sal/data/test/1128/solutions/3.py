a, m = input().split(' ')
a, m = int(a), int(m)
d = set()
d.add(a % m)

while a % m != 0:
    a += a % m
    if a % m in d:
        print('No')
        break

    d.add(a % m)

if not a % m:
    print('Yes')
