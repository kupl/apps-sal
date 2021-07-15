n, m = list(map(int, input().split()))
x_s = list(map(int, input().split()))



if n >= m:
    print((0))
else:
    x_s.sort()
    b=[]
    for i in range(m-1):
        b.append(x_s[i+1]-x_s[i])
    b.sort()
    ans = 0
    for i in range(m-n):
        ans += b[i]
    print(ans)

