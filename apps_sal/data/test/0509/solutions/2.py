n = int(input())
a = [int(input()) for _ in range(n)]
ok = False
for i in range(2 ** n):
    bi = bin(i)[2:]
    bi = '0' * (n - len(bi)) + bi
    if sum(((-1 if bi[j] == '0' else 1) * a[j] for j in range(n))) % 360 == 0:
        ok = True
print('YES' if ok else 'NO')
