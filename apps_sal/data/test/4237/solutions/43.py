a,b,c,d = map(int,input().split())

from math import gcd

lcm = (c*d)//gcd(c,d)

b_div_c = b//c
a_div_c = (a-1)//c

b_div_d =b//d
a_div_d = (a-1)//d

b_div_cd = b//lcm
a_div_cd = (a-1)//lcm



ans1 = b_div_c - a_div_c
ans2 = b_div_d - a_div_d
ans3 = b_div_cd - a_div_cd

ans = b -(a-1) - ans1 - ans2 + ans3
print(ans)
