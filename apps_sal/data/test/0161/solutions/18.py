import math
x = int(input().strip())
ss = ""
num = 0
nu = 0
while(True):
    n = math.floor(math.log(x, 2))
    nt = (2**(n + 1)) - 1
    if(x == nt):
        break
    if(num == 0):
        x = x ^ (nt)
        ss = ss + str(n + 1) + " "
    else:
        x = x + 1
    num = 1 - num
    nu = nu + 1
print(nu)
print(ss)
