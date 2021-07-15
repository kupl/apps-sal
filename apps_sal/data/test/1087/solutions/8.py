import sys,math,collections,itertools
input = sys.stdin.readline

N,K=list(map(int,input().split()))
A=list(map(int,input().split()))
maxA = max(A)
binK = bin(max(maxA,K))[2:]
num_one = [0]*len(binK)
for k in range(len(binK)):
    for a in A:
        num_one[len(binK)-k-1] += a>>k & 1
ans = 0
flag = False#Kより小さいことが確定したらTrue

for k in range(len(binK)):
    if flag:#小さいことが確定していたら、どっちか大きいほうを採用する
        if num_one[k] > N-num_one[k]:#1立ってる数が多かったら、0にしとく
            ans += pow(2,len(binK)-k-1)*(num_one[k])
        else:
            ans += pow(2,len(binK)-k-1)*(N-num_one[k])
    else:#小さいことが確定していないなら K>>len(binK)-k-1が0なら 0 そうじゃないなら、お得な方で0ならTrueにする
        if K>>len(binK)-k-1 &1:
            if num_one[k] > N-num_one[k]:#1立ってる数が多かったら、0にしとく
                flag = True
                ans += pow(2,len(binK)-k-1)*(num_one[k])
            else:
                ans += pow(2,len(binK)-k-1)*(N-num_one[k])#1立ってる数が少ないなら、1立ててFlagは未定状態
        else:
            ans += pow(2,len(binK)-k-1)*(num_one[k])

print(ans)
                
            

