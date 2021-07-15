import math

X,Y = list(map(int,input().split()))

power = 0
while X * pow(2,power) <= Y:
    power += 1
print(power)

