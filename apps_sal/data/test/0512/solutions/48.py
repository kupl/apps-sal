import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")

n = int(input())
ab = [tuple(map(int, input().split())) for _ in range(n)]
t = [None]*(2*n)
ans = None
for a,b in ab:
    if a>0 and b>0:
        if t[a-1] is not None or a>=b:
            ans = -1
            break
        if t[b-1] is not None:
            ans = -1
            break
        t[a-1] = (1, b-a)
        t[b-1] = (2, b-a)
    elif a>0:
        if t[a-1] is not None:
            ans = -1
            break
        t[a-1] = (1, None) # 乗った
    elif b>0:
        if t[b-1] is not None:
            ans = -1
            break
        t[b-1] = (2, None) # 降りた
if ans==-1:
    print("No")
else:
    for i in range(len(t)):
        if t[i] is None:
            t[i] = (0, None)
    dp = [False]*(2*n+1) # i番目の直後で仕切れるか
    dp[0] = True
    def sub(j,i):
        if (i-j)%2==1:
            return False
        for k in range((i-j)//2):
            if t[j+k][0]==2 or t[j+(i-j)//2+k][0]==1:
                return False
            elif t[j+k][1] is not None and t[j+k][1]!=(i-j)//2:
                return False
            elif t[j+(i-j)//2+k][1] is not None and t[j+(i-j)//2+k][1]!=(i-j)//2:
                return False
            elif t[j+k][0]!=0 and t[j+k][1] is None and t[j+k+(i-j)//2][0]!=0:
#                 print(j,k,i)
                return False
            elif t[j+(i-j)//2+k][0]!=0 and t[j+(i-j)//2+k][1] is None and t[j+k][0]!=0:
#                 print(j,k,i)
                return False
        return True
    for i in range(1,2*n+1):
        val = False
        for j in range(i):
            if dp[j] and sub(j,i):
                val = True
        dp[i] = val
    if dp[2*n]:
        print("Yes")
    else:
        print("No")
