from sys import stdin

tt = int(stdin.readline())

for loop in range(tt):

    a,b,x,y,n = map(int,stdin.readline().split())

    ans = float("inf")

    if a-x + b-y < n:
        print (x*y)
        continue
    
    #first a
    if a-x >= n:
        ans = min(ans , (a-n) * b)
    else:
        rem = n - (a-x)
        ans = min(ans , x * (b-rem))

    #b
    if b-y >= n:
        ans = min(ans , (b-n) * a)
    else:
        rem = n - (b-y)
        ans = min(ans , y * (a-rem))

    print (ans)
