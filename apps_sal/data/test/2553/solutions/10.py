import math
t = int(input())
for i in range(t):
    n, x = list(map(int, input().split()))
    a = list(map(int, input().split()))
    evencount = 0
    oddcount = 0
    for j in range(n):
        if a[j] % 2 == 0:
            evencount += 1
        else:
            oddcount += 1
    if oddcount == 0:
        print('No')
    elif evencount == 0:
        if x % 2 == 1:
            print('Yes')
        else:
            print('No')
    else:
        if x < n:
            print('Yes')
        elif oddcount % 2 == 1:
            print('Yes')
        else:
            print('No')
