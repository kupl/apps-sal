t = int(input())

while t:
    t -= 1
    n, x = map(int, input().split())
    a = list((-1 if int(i) else 1) for i in input())
    s = [0] * n
    s[0] = a[0]
    for i in range(1, n):
        s[i] = s[i - 1] + a[i]
    
    
    if s[-1] == 0:
        if x in s:
            print(-1)
        else:
            print(0)
    else:
        res = 1 if (x == 0) else 0
        for i in range(n):
            gap = x - s[i]
            if gap % s[-1] == 0 and gap // s[-1] >= 0:
                res += 1
        print(res)        
