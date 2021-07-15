n, k = map(int, input().split())
MOD =10**9+7

memo = [[{} for j in  range(n+1)] for i in range(n+1)]

def fdp(cur_N, remain, min_k, MOD=10**9+7):
    if cur_N <= 1:
        if remain == 0 and min_k == 0:
            return 1
        if remain == 1 and min_k == 2:
            return 1
        else:
            return 0
    if min_k in memo[cur_N][remain]:
        ret = memo[cur_N][remain][min_k]
        return ret
    
    temp1 = fdp(cur_N-1, remain, min_k - 2*remain) %MOD
    temp2 = fdp(cur_N-1, remain+1, min_k -2*remain) %MOD
    temp3 = fdp(cur_N-1, remain-1, min_k-2*remain) % MOD
    score = (temp1*(2*remain+1))%MOD +(temp2*(remain+1)*(remain+1))%MOD+temp3
    score = score % MOD
    memo[cur_N][remain][min_k] = score
    return score
ret = fdp(n, 0, k)
print(ret)
