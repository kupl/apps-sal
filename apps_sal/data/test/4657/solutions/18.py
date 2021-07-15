import sys
 
t = int(input())
for i in range(t):
    n, k = list(map(int, sys.stdin.readline().split()))
    a = list(map(int, sys.stdin.readline().split()))
    p = []
    for i in range(n):
        if a[i] % 2 == 1:
            p.append(i+1)
    if len(p) >= k and (len(p) - k)%2 == 0:
        p = p[:k]
        p[len(p)-1] = n
        print('YES')
        print(*p)
    else:
        print('NO')

