import math
A,B,C,D = list(map(int,input().split()))

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

lcm = lcm(C,D)

u_b_ans = (B//C + B//D) - B//lcm
u_a_ans = ((A-1)//C + (A-1)//D) - (A-1)//lcm

print((B-A+1 - u_b_ans + u_a_ans))

