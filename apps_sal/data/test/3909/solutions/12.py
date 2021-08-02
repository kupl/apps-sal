n = int(input())
r = 3
while(1):
    if(n % r):
        print((n - 1) // r + 1)
        break
    else:
        r *= 3
