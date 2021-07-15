import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def LcpByZ(target):
    len_t = len(target)
    lcp = [-1] * len_t
    top = 1  # 右の箱において、左の箱の0に対応する点
    left = 0  # 左の箱の左端(本当はここでので宣言は不要だけど理解の為)
    right = 0  # 左の箱の右端
    lcp[0] = 0
    while top < len_t:
        # 箱を右に広げていく
        while top + right < len_t and target[right] == target[top + right]:
            right += 1
        # 右の箱左端のlcpを記録
        lcp[top] = right
        left = 1
        # 箱の幅が0だったらtopを動かして、このターン終了
        if right == 0:
            top += 1
            continue
        # lcpを記録しながら箱を左に縮めていく（最初の条件重要）
        while left + lcp[left] < right and left < right:
            lcp[top + left] = lcp[left]
            left += 1
        # topを右の箱の左端にして、左の箱を0まで戻す
        top += left
        right -= left
        left = 0  # これも本当は不要
    return lcp

def dfs(i,si):
    dp[i]=0
    ni=(i+tn)%sn
    if lcp[tn+1+ni]!=tn:return False
    if ni==si:return True
    if dp[ni]==-1 and dfs(ni,si):return True
    dp[i]=dp[ni]+1

s=SI()
t=SI()
ss = s
while len(ss) < len(s) + len(t): ss += s
lcp = LcpByZ(t + "@" + ss)
sn = len(s)
tn = len(t)
dp=[-1]*sn
for i in range(sn):
    if dp[i]!=-1:continue
    if dfs(i,i):
        print(-1)
        return
print(max(dp))

