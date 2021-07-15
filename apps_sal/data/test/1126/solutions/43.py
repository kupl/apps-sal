#高々Mの繰り返し
N,X,M =list(map(int,input().split()))
memo = [0]*(2*M+1)#最長2Mまでloopするはず
val_idx = {X:1}#loopしたときに、どこがloop開始のインデックスかを知るためのメモ
seen = set([X])#見た判定。o(1)で判定するため
memo[1]=X#累積和を取っておく

loop_length = 0#loopしたか、したならloop長はなにか
for i in range(2,N+1):
    X = (X**2)%M
    if X not in seen:#まだloopしてない
        seen.add(X)
        val_idx[X]=i
        memo[i]+=memo[i-1]+X
    else:#loopした
        loop_start_val = X
        loop_start_idx = val_idx[X]
        loop_length = i-loop_start_idx
        break
if loop_length == 0:#ループしなかったら、N番目
    print((memo[N]))
else:#ループしたなら
    rest_num = (N-loop_start_idx+1)%loop_length#ループの後ろのきれっぱし
    loop_num =(N-loop_start_idx+1)//loop_length#ループ回数
    ans = (memo[loop_start_idx+loop_length-1]-memo[loop_start_idx-1])*loop_num+memo[loop_start_idx-1+rest_num]#1ループの和 x ループ回数＋きれっぱし
    print(ans)

