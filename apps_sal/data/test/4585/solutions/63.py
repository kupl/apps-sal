import math

def goukei(n):
    return int(n*(n+1)/2)

x = int(input())
tmp = int(math.sqrt(2 * x))
#print(tmp,goukei(tmp))
while goukei(tmp)<x:
    tmp += 1

print(tmp)
