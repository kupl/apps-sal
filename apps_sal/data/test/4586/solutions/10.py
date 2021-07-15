# 079_a
N=int(input())
# if 1<=N and N<=9999:
#
n=str(N)
if (n[0]==n[1] and n[1]==n[2]) or (n[1]==n[2] and n[2]==n[3]):
    print('Yes')
else:
    print('No')
