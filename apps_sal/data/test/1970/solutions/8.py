3
n = int(input())
for _ in range(n):
    k = []
    b = []
    for i in range(8):
        s = input()
        for j in range(8):
            if s[j] == 'K':
                k.append((i, j))
    print('YES' if abs(k[0][0] - k[1][0]) % 4 == 0 and abs(k[0][1] - k[1][1]) % 4 == 0 else 'NO')
    if _ < n - 1:
        input()
