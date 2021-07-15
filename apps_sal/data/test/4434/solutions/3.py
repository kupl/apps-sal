
t = int(input())

for loop in range(t):

    n = int(input())

    ans = 0
    for i in range(n//2+1):
        ans += i * ( (i*2+1)**2 - (i*2-1)**2 )

    print (ans)

