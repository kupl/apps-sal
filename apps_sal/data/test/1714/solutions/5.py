n, k = [int(x) for x in input().split()]

for i in range(1, n+1):
    if i<=k:
        print(2*i-1, end=' ')
        print(2*i, end=' ')
    else:
        print(2*i, end=' ')
        print(2*i-1, end=' ')

