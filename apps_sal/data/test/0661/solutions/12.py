import sys
input = sys.stdin.readline

M,K = list(map(int,input().split()))

if M==1:
    if K==0:
        print((0,0,1,1))
    else:
        print((-1))
else:
    if K >= (1<<M):
        print((-1))
    else:
        a = list(range(1<<M))
        a.remove(K)
        ans = a + [K] + a[::-1] + [K]
        print((" ".join(map(str,ans))))

