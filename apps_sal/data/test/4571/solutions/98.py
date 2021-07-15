N,M = map(int,input().split())
fixT1 = 100*(N-M)
fixT2 = 1900*(M)
trynum = 2**M
print((fixT1+fixT2)*trynum)
