import sys
input = lambda: sys.stdin.readline().strip()

n, k = list(map(int, input().split()))
S = list(input())
if n==1 and k==1: print(0)
elif k==0: print(''.join(S))
else:
    cnt = 0
    if S[0]!='1':
        S[0] = '1'
        cnt+=1
    for i in range(1, n):
        if cnt==k: break
        if S[i]!='0':
            S[i] = '0'
            cnt+=1
    print(''.join(S))

