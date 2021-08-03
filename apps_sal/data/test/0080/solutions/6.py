from math import gcd, sqrt
l, r, x, y = list(map(int, input().split()))
product = x * y
div = int(sqrt(product))
div = ((div // x) * x)
ans = 0
while(div >= 1):
    if(product % div == 0):
        div2 = product // div
        hcf = gcd(div, div2)
        lcm = (div * div2) // hcf
        if(hcf == x and lcm == y):
            if(div >= l and div <= r and div2 >= l and div2 <= r):
                ans += 2
                if(div2 == div):
                    ans -= 1
            else:
                break
    div -= x
print(ans)
