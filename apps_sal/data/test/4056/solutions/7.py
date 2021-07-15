
import math

def divs(x):
    ans = 0
    d = 1
    while d*d <= x:
        if x%d == 0:
            ans += 2
            ans -= (d*d==x)
        d+= 1
    return ans

n = int(input())
arr = [int(x) for x in input().split()]

gcd = arr[0]
for a in arr:
    gcd = math.gcd(a,gcd)


print(divs(gcd))


