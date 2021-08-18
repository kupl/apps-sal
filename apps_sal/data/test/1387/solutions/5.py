n, t = map(int, input().split())
a = [int(x) for x in input().split()]

p = 1

while p <= t:
    if p == t:
        print('YES')
        quit()
    p += a[p - 1]

print('NO')
