(a, b, c) = map(int, input().split())
modb = [0] * 100
for i in range(1, 100000):
    n = a * i
    m = n % b
    if modb[m] != 0:
        break
    modb[m] = 1
print('YES' if modb[c] == 1 else 'NO')
