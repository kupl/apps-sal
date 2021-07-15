import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")

n = int(input())
caa,cab,cba,cbb = [input() for _ in range(4)]
M = 10**9+7
done = False
def swap(w):
    if w=="A":
        return "B"
    else:
        return "A"
if cab=="B":
    caa,cab,cba,cbb = swap(caa), swap(cab), swap(cba), swap(cbb)
    done = True
if (not done and caa=="A") or (done and cbb=="A"):
    ans = 1
else:
    if n==2:
        ans = 1
    else:
        if cba=="B":
            ans = pow(2, n-3, M)
        else:
            def sub(n):
                dp0 = [0]*(n-2)
                dp1 = [0]*(n-2)
                dp1[0] = 1
                for i in range(1,n-2):
                    dp0[i] = dp1[i-1]
                    dp1[i] = dp1[i-1] + dp0[i-1]
                    dp0[i] %= M
                    dp1[i] %= M
                ans = dp0[n-3] + dp1[n-3]
                ans %= M
#                 print(dp0, dp1)
                return ans
            ans = sub(n)%M
print(ans%M)
