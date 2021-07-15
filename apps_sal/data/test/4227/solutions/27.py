N,M = list(map(int,input().split()))


#iから進める場所をリストにして保管
edges = {i:[] for i in range(1,N+1)}
for i in range(M):
  a,b = list(map(int,input().split()))
  edges[a].append(b)
  edges[b].append(a)


#深さ優先探索
def dfs(list):
    #lst(通過点)の数がN(頂点数)と等しくなったら探索終了（成功）
  if len(list) == N:
    return 1
  else:
    a = list[-1]
    #lstの最後尾（現在地）が次に進める場所をnextとしてリスト化
    #nextに以前通った場所が入っていないか確認
    next = [n for n in edges[a] if n not in list]
    #次に進める場所がなくなったら探索終了（失敗）
    if len(next) == 0:
      return 0

    total = 0
    #再帰でさらに探索
    for n in next:
      total += dfs(list + [n])

    return total


ans = dfs([1])

print(ans)

