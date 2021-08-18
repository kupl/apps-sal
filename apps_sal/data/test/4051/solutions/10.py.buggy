n = int(input())
a = list(map(int, input().split()))

for i in range(len(a) - 1):
    if abs(a[i + 1] - a[i]) > 1:
        print('NO')
        return

while len(a) > 0:
    m = max(a)
    i = a.index(m)
    a.remove(m)
    if 0 < i < len(a) and abs(a[i] - a[i - 1]) > 1:
        print('NO')
        return

print('YES')
