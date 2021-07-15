d, g = map(int, input().split())
pc = [0] + [list(map(int, input().split())) for i in range(d)]
def dfs(ind,score):
  if ind == 0:
    return float("inf")
  cnt = min(score//(ind*100),pc[ind][0])
  add_sc = cnt*(ind*100)
  if cnt == pc[ind][0]:
    add_sc += pc[ind][1]
  if add_sc < score:
    cnt += dfs(ind-1,score-add_sc)
  return min(cnt,dfs(ind-1,score))
 
print(dfs(d,g))
