n = int(input())
a = list(map(int, input().split()))

if a.count(0) == n or a.count(1) == n:
    print('YES')
    return

w = a.index(not a[0])

if n % w != 0:
    print('NO')
    return

for i in range(n // w):
    if a[w * i: w * (i + 1)] != [(i % 2 + a[0]) % 2 for _ in range(w)]:
        print('NO')
        return

print('YES')
