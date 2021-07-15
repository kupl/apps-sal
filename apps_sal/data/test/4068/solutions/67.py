N,M = map(int,input().split())
A = [int(input()) for i in range(M)]
n = 0
if M != 0:
    a = b = A[0]
else:
    a = b = -2
c = 0
ans = [0,1]
for i in range(1,N+1):
    if  i == a:
        c = 0
        n += 1
        b = a
        if n <= M-1:
            a = A[n]
    elif i-2 == b:
        c = ans[-1]
    elif i-1 == b :
        c = ans[-2]
    else:
        c  = ans[-1] + ans[-2]
    c %= 10**9 + 7
    ans.append(c)
print(ans[-1])
