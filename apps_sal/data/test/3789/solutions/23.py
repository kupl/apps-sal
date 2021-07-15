import networkx as nx

N=int(input())
*A,=map(int,input().split())
INF = 10**20

G = nx.DiGraph()
G.add_nodes_from(range(N+2))
for i in range(N):
  if A[i]<0:
    G.add_edge(0,i+1,capacity=-A[i])
    G.add_edge(i+1,N+1,capacity=0)
  else:
    G.add_edge(0,i+1,capacity=0)
    G.add_edge(i+1,N+1,capacity=A[i])
  
for i in range(1,N//2+1):
  for j in range(i,N+1,i):
    G.add_edge(i,j,capacity=INF)
    
flow_value,flow_dict = nx.maximum_flow(G,0,N+1)
print(sum(filter(lambda x: x>0,A))-flow_value)
