import sys
sys.setrecursionlimit(10**6)

a, b = map(int, input().split())

def calc(a):
    if a <= 0: return 0
    
    # 4のときに0,1,2,3,4までになるので、これは5つの整数
    a += 1
    
    ans = 0
    # i桁目の偶奇を調べる
    # 10^3 <= 2^10
    # 10^12 <= 2進数で40桁くらい
    for i in range(50):
        
        # 0桁目 周期2, 1桁目 周期4, 2桁目 周期8
        loop = (1 << (i+1))
        cnt = a//loop * loop//2 # loopした回数×1が出てくる回数
        # 0000....001111....11
        cnt += max(0, (a%loop) - (loop//2))
        # その桁の1の数が奇数だったら足し算
        if cnt%2 == 1:
            ans += 1<<i
            
    return ans
        
ans = calc(a-1)^calc(b)

print(ans)
