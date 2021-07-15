from math import log

##n = int(input())
##
####print(n-1 + int(log(n-1)/log(2)))
##
##def ord2(n): ## max power of 2 that divides n
##    ret = 1
##
##    while n%ret == 0:
##        ret*=2
##
##    return ret//2
##
##total = 0
##
##for i in range(1, n):
##    total += ord2(i)

# fast way?

n = int(input()) - 1

divider = 2**int(log(n)/log(2))
total = 0
doubled = 0

while divider > 0:

    total += (n//divider - doubled)*divider

    ##print('A total of', n//divider, 'work, and the number of doubled', doubled)
    
    doubled += n//divider - doubled

    divider //=2

##    total = 0
##    power = 0
##
##    while 2**power <= n:
##
##        total += n//(2**power)
##
##        power += 1

print(total)

