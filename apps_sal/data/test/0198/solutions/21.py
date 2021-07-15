import math;

n = int(input());

if(n%2!=0):
    print(0);
else:
    print(math.ceil(n/4)-1);
