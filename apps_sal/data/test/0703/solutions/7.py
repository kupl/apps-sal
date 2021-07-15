sections,nuts,divisors,cap = list(map(int,input().split()))
boxes=0
while(nuts > 0):
    s = 1
    if(divisors > 0 and divisors <= sections -1):
        s = divisors + 1
        divisors = 0
    elif divisors > sections -1:
        s = sections
        divisors -= (sections -1)
    nuts -= (s*cap)
    boxes+=1
print(boxes)

