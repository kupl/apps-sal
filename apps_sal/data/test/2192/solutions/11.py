mat = []
num = int(input())
for k in range(num):
    s = input().split()
    mat.append(list(map(int, s)))
for k in range(num):
    for l in range(num):
        print('%.8f' % ((mat[k][l] + mat[l][k]) / 2), end=' ')
    print(end='\n')
for k in range(num):
    for l in range(num):
        print('%.8f' % ((mat[k][l] - mat[l][k]) / 2), end=' ')
    print(end='\n')
