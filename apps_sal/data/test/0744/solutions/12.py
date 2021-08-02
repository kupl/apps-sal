n = int(input())
a = input()
s, f = 0, 0
for i in range(n - 1):
    if a[i] == 'S' and a[i + 1] == 'F':
        f += 1
    if a[i] == 'F' and a[i + 1] == 'S':
        s += 1
print('YES' if f > s else 'NO')
