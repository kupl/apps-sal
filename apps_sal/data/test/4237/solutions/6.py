import math
def lcm(x, y):
    return (x * y) // math.gcd(x, y)

def main():
    A,B,C,D = list(map(int,input().split()))
    #Cで割り切れる数の探索
    tmpC = (A-1)//C
    tmpC2 = (B)//C
    numC = tmpC2 - tmpC
    #Dで割り切れる数の探索
    tmpD = (A-1)//D
    tmpD2 = (B)//D
    numD = tmpD2 - tmpD
    #CでもDで割り切れるもの
    if C == D:
        ans = B-A+1-numC
    else:
        tmpCD = (A-1)//lcm(C,D)
        tmpCD2 = (B)//lcm(C,D)
        numCD = tmpCD2 - tmpCD
        ans = B-A+1-numC-numD+numCD
    return ans
print((main()))

