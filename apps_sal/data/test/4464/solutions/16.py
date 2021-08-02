a, b, c = map(int, input().split())
d = a % b
for i in range(b):
    if (d * i) % b == c:
        print('YES')
        return
print('NO')
