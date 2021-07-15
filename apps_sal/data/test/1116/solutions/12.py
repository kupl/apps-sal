n = int(input())

def gcd(x,y):
    
    while x != 0 and y != 0:
        x,y = max(x,y), min(x,y)
        x %= y
    return max(x,y)

for i in range(n):

    r, b, k = list(map(int,input().split()))
    g = gcd(r, b)
    r,b = max(r,b)//g, min(r,b)//g
    if (r % b == 0 and r // b - 1 < k) or (r % b == 1 and r // b < k) or \
        (r % b > 1 and r // b + 1 < k):
        print("OBEY")
    else:
        print("REBEL")

