a = int(input())
b = list(map(int, input().split()))
d = set(b)
if len(d) != a:
    print('NO')
    return
ima = 0
for i in range(a):
    if b[ima] < b[i]:
        ima = i
for i in range(1, ima):
    if b[i] < b[i - 1]:
        print('NO')
        return
for i in range(ima, a - 1):
    if b[i] < b[i + 1]:
        print('NO')
        return
print('YES')
