#高々Mの繰り返し
N,X,M =list(map(int,input().split()))
memo = [0]*(2*M+1)
val_idx = {X:1}
idx_val = {1:X} 
seen = set([X])
memo[1]=X

loop_length = 0
for i in range(2,N+1):
    X = pow(X,2,M)
    if X not in seen:#まだloopしてない
        seen.add(X)
        val_idx[X]=i
        idx_val[i]=X
        memo[i]+=memo[i-1]+X
    else:#loopに達した
        loop_start_val = X
        loop_start_idx = val_idx[X]
        loop_length = i-loop_start_idx
        break
if loop_length == 0:
    print((memo[N]))
else:
    rest_num = (N-loop_start_idx+1)%loop_length
    loop_num =(N-loop_start_idx+1)//loop_length
    ans = (memo[loop_start_idx+loop_length-1]-memo[loop_start_idx-1])*loop_num+memo[loop_start_idx-1+rest_num]
    print(ans)

