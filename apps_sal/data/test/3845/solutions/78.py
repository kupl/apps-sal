# editorial参照
# 格子まで詰め込もうとしたのが困難
# 十分大きい黒白の塊一つに孤立した白黒の点を取る

#最初のに出力h,w追加
a,b = list(map(int, input().split( )))
k=50
W = [["."]*(k*2) for i in range(k)] 
B = [["#"]*(k*2) for i in range(k)]

for i in range(b-1):
    w = (i//k)*2
    h = (i%k)*2
    W[w][h]="#"


for i in range(a-1):
    w = (i//k)*2+1
    h = (i%k)*2+1
    B[-w][-h]="."
ans = [''.join(W[i]) for i in range(k)]+ [''.join(B[i]) for i in range(k)]
print((100,100))
print(('\n'.join(ans)))


    

