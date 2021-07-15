from networkx import *
h,w=map(int,input().split());r=range(10);G=DiGraph();G.add_nodes_from(r);C=[[*map(int,input().split())]for _ in r];G.add_weighted_edges_from([(i,j,C[i][j])for i in r for j in r]);S=[single_source_dijkstra_path_length(G,i)[1]for i in r];A=[[*map(int,input().split())]for _ in "_"*h];print(sum(S[abs(x)] for a in A for x in a))
