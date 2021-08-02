str_params = input()
params = [int(s) for s in str_params.split(' ')]
n = params[0]
k = params[1]
part = 0;
if (k > n**2):
    print(('%d\n' % (-1)));
else:
    matr = [[0 for x in range(n)] for y in range(n)]
    i = 1
    while part < k:
        matr[i - 1][i - 1] = 1
        part = part + 1
        j = i
        while (k - part > 1) & (j < n):
            #print (i-1, j)
            matr[i - 1][j] = 1
            matr[j][i - 1] = 1
            j = j + 1
            part = part + 2
        i = i + 1;
    for row in matr:
        print(' '.join(map(str, row)))
    print()
