# E - Divisible Substring
N,P = map(int,input().split())
S = input()
ans = 0
if P==2 or P==5:
    for i in range(N):
        if int(S[i])%P==0:
            ans += i+1
else:
    l = [1]+[0]*(P-1)
    tmp = 0
    r10 = 1
    for i in range(N-1,-1,-1):
        tmp = (r10*int(S[i])+tmp)%P
        l[tmp] += 1
        r10 = (r10*10)%P
    for x in l:
        ans += x*(x-1)//2
print(ans)
