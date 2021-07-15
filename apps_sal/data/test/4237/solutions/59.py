import math
 
def lcm(x, y):
    return (x * y) // math.gcd(x, y)
 
a,b,c,d=map(int,input().split())
 
c_div=(b//c)-((a-1)//c)
d_div=(b//d)-((a-1)//d)
cd_div=(b//lcm(c,d))-((a-1)//lcm(c,d))
 
ans=(b-a+1)-((c_div)+(d_div)-(cd_div))
print(ans)
