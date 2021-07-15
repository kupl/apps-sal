S=str(input())
maru_count=0
#注文書に書かれた文字列Sに含まれるoの数だけ、１００円加算する。

for i in S:
    if i=='o':
        maru_count=maru_count+1
    elif i=='x':
        maru_count=maru_count+0
        
    
ramen_price=700+100*maru_count

print(ramen_price)
