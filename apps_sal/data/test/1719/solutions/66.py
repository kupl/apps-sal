n=int(input())
mod1,mod2=10**9+7,998244353
mod=mod1
import sys
sys.setrecursionlimit(10**9)
memo=[{}for i in range(n+1)]
def ok(s):
    if "AGC"in s:return False
    for i in range(3):
        if "AGC"in s[:i]+s[i+1]+s[i]+s[i+2:]:
            return False
    return True
def dfs(cnt,las):
    if las in memo[cnt]:return memo[cnt][las]
    if cnt==n:return 1
    ret=0
    for nec in "AGCT":
        if ok(las+nec):
            ret=(ret+dfs(cnt+1,las[1:]+nec))%mod
    memo[cnt][las]=ret
    return ret
print(dfs(0,"TTT"))
