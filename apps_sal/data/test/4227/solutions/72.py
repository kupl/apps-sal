n,m=list(map(int,input().split()))
#隣接リスト表現
es=[[0 for i in range(n)] for i in range(n)]
for i in range(m):
  a,b=list(map(int,input().split()))
  es[a-1][b-1]=1
  es[b-1][a-1]=1

# 再帰の深さが1000を超えそうなときはこれをやっておく
import sys
sys.setrecursionlimit(10**7)


#深さ優先探索
#n個の頂点が未探索であるとしておく
visited=[0 for i in range(n)]
check=[1 for i in range(n)]

def dfs(v,visited):
  #ansは頂点vから始まるパスの数
  ans=0
  #自分がいることろを探索済にしておく
  visited[v-1]=1

  if visited==check:
    visited[v-1]=0
    return 1
  #そこから行けるところに対して深さ優先探索
  for i in range(n):
    #つながっていて未探索
    if es[v-1][i]==1 and visited[i]==0:
        ans+=dfs(i+1,visited)
  #全部探索し終わったら今自分がいるところは未探索に戻しておく
  visited[v-1]=0
  return ans

print((dfs(1,visited)))

