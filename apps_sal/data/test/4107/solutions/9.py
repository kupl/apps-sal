def find(roomcount,radius,string):
    zero_roomcount=[0]*(roomcount+1)
    binary_move=1<<1000#сдвиг двоичной единицы на 1000 влево или любое число
    for i in range(roomcount,0,-1):
        if string[i-1]=='1':
            binary_move=i
        zero_roomcount[i]=binary_move
    dp=[0]
    for i in range(1,roomcount+1):
        dp.append(dp[-1]+i)
        c=zero_roomcount[max(i-radius,1)]
        if c<=i+radius:
            dp[i]=min(dp[i],dp[max(1,c-radius)-1]+c)  
    return dp[roomcount]
roomcount,radius=map(int,input().split())
string=input()
print(find(roomcount,radius,string))
