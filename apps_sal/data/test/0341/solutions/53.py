N,K = map(int,input().split())
R,S,P = map(int,input().split())
T = list(input())
 
for n in range(N-K):
  if T[n+K]==T[n]:
    T[n+K]=""
    
print(P*T.count("r")+R*T.count("s")+S*T.count("p"))
