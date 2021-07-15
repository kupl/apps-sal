import sys
n , k = map(int,input().split())

if (k*(k-1)) < n:
    print('NO')
else:
    print('YES')
    c = 0
    d = 1
    for i in range(n):
        if c == k:
            d += 1
            c = 0
        if d == k:
            break
        print(c+1 , (c+d)%k + 1)
        c += 1
