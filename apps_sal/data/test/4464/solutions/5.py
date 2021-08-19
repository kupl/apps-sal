(A, B, C) = map(int, input().split())
amari = []
for i in range(1, B + 1):
    amari.append(A * i % B)
print('YES' if C in amari else 'NO')
