from networkx import*
H,*S=open(0)
H,W=map(int,H.split())
g=Graph()
for i in range(m:=H*W):g.add_weighted_edges_from([[m*2,h:=i//W,I:=m*3],[m*2,w:=i%W+m,I]]*((c:=S[h][w-m])=='S')+[[h,I,I],[w,I,I]]*(c=='T')+[[h,w,1],[w,h,1]]*(c>'T'))
print([-1,f:=minimum_cut(g,m*2,I,'weight')[0]][f<I])
