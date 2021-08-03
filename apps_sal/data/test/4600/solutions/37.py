N, M = map(int, input().split())
num_AC, num_WA = 0, 0
res = [list(input().split()) for i in range(M)]
check = ['v'] * N
WA_check = [0] * N
for i, j in res:
    i = int(i)
    if check[i - 1] == 'v':
        if j == 'WA':
            WA_check[i - 1] += 1
        if j == 'AC':
            num_AC += 1
            num_WA += WA_check[i - 1]
            check[i - 1] = '.'
print(num_AC, num_WA)
