n = int(input())
A = []
A.append(list('+------------------------+'))
A.append(list('|
A.append(list('|
A.append(list('|
A.append(list('|
A.append(list('+------------------------+'))
for k in range(n):
    j=i=1
    while A[i][j] != '
        i=1
        while i < 5 and A[i][j] != '
            i += 1
        if A[i][j] != '
            j += 2
    A[i][j]='O'
for line in A:
    print(''.join(line))
