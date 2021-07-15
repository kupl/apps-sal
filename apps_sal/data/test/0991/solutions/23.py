from heapq import heappop,heappush

def main():
    N,M,S=map(int,input().split())
    G=[[] for _ in range(N)]
    for i in range(M):
        U,V,A,B=map(int,input().split())
        G[U-1].append([V-1,A,B])
        G[V-1].append([U-1,A,B])
    C=[]
    D=[]
    for _ in range(N):
        c,d=map(int,input().split())
        C.append(c)
        D.append(d)

    MaxMoney=2500

    dp=[[float('inf') for __ in range(MaxMoney+1)] for _ in range(N)]

    cost=0
    money=min(S,MaxMoney)
    que=[]
    heappush(que,(cost,0,money)) #cost,node,money
    dp[0][money] = 0

    while len(que)>0:
        cost,node,money=heappop(que)

        stop_money=min(money+C[node],MaxMoney)
        stop_cost=cost+D[node]
        if stop_cost<dp[node][stop_money]:
            dp[node][stop_money]=stop_cost
            heappush(que,(stop_cost,node,stop_money))

        for to_node,to_money,to_cost in G[node]:
            money_=min(money-to_money,MaxMoney)
            if money_<0:
                continue
            cost_=cost+to_cost
            if dp[to_node][money_]<=cost_:
                continue

            dp[to_node][money_]=cost_
            heappush(que,(cost_,to_node,money_))

    for i in range(1,N):
        print(min(dp[i]))




def __starting_point():
    main()
__starting_point()
