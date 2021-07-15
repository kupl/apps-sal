import math

A,B,C,D = list(map(int,input().split()))
divAC,modAC = divmod(A,C)
divBC,modBC = divmod(B,C)
ans = 0
if modAC == 0:
    ans += divBC - divAC + 1
else:
    ans += divBC - divAC

divAD,modAD = divmod(A,D)
divBD,modBD = divmod(B,D)
if modAD == 0:
    ans += divBD - divAD + 1
else:
    ans += divBD - divAD
divACD,modACD = divmod(A,int(C * D / math.gcd(C, D)))
divBCD,modBCD = divmod(B,int(C * D / math.gcd(C, D)))
if modACD == 0:
    ans -= divBCD - divACD + 1
else:
    ans -= divBCD - divACD

print((B-A+1-ans))


