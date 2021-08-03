

n = int(input())
inp = input()
sl, sr, qr, ql = 0, 0, 0, 0


for i in range(len(inp) // 2):
    if inp[i] == '?':
        ql += 1
    else:
        sl += int(inp[i])

for i in range(n // 2, n):
    if inp[i] == '?':
        qr += 1
    else:
        sr += int(inp[i])


if(sl - sr == 9 * (qr - ql) / 2):
    print('Bicarp')
else:
    print('Monocarp')
