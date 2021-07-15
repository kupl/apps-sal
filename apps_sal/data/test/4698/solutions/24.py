N=int(input())
T=input()
M=int(input())
P=[input() for i in range(M)]

def ans050(N:int, T:str, M:int, P:list):
    T_list=list(map(int,T.split()))
    ans_list=[]
    for i in range(M):
        T_list = list(map(int, T.split()))
        P_list=list(map(int,P[i].split()))
        del T_list[P_list[0]-1]
        T_list.append(P_list[1])
        ans_list .append(sum(T_list))
    return ans_list
for i in range(M):
    print((ans050(N,T,M,P))[i])
