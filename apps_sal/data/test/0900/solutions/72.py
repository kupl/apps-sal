# -*- coding: utf-8 -*-

R10 = list(range(10))
R13 = list(range(13))

S = input()
R = [[(M-N)*4 % 13 for N in R10] for M in R13]
AM = 10**9+7

MOD =[1]+[0]*12

for D in S:
    if D == '?':
        MOD = [sum([MOD[N] for N in M])%AM for M in R]
    else:
        C = int(D)
        MOD = [MOD[M[C]] for M in R]
    #end if
#end for

print((MOD[5]))

