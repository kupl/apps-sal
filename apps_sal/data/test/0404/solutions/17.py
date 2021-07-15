from math import sqrt
def countDivisors(n):
    cnt=0
    for i in range(1,(int(sqrt(n)))+1):
        if(n%i==0):
            if(n/i==i):
                cnt = cnt + 1
            else:
                cnt = cnt + 2
    return cnt

n=int(input())
print(countDivisors(n))

