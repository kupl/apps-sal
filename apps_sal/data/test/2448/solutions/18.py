t = int(input())
for i in range(t):
    n = int(input())
    a, b, c = list(map(int, input().split()))
    d = list(input())
    ans = 0
    ansarr = ['0' for x in range(n)]
    ansstr = ''
    for j in range(n):
        if d[j] == 'R' and b > 0:
            b -= 1
            ans += 1
            ansarr[j] = 'P'
        elif d[j] == 'P' and c > 0:
            c -= 1
            ans += 1
            ansarr[j] = 'S'
        elif d[j] == 'S' and a > 0:
            a -= 1
            ans += 1
            ansarr[j] = 'R'
    for j in range(n):
        if ansarr[j] == '0':
            if a > 0:
                a -= 1
                ansstr += 'R'
            elif b > 0:
                b -= 1
                ansstr += 'P'
            else:
                c -= 1
                ansstr += 'S'
        else:
            ansstr += ansarr[j]
    if ans >= n / 2:
        print("YES")
        print(ansstr)
    else:
        print("NO")
