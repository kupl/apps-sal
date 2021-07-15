import sys
readline = sys.stdin.readline

N,A,B,C = list(map(int,readline().split()))

val = [A,B,C]
# 0,0を作ってはいけない
# 基本的には小さいほうに1を足す
# 両方とも1の場合は、次の操作で選ばれるほうに1を足す
# 両方とも次の操作で選ばれるときはどちらに足してもよい

S = [readline().rstrip() for i in range(N)]
ans = []

def get_ind(s):
  res = []
  for c in s:
    if c == "A":
      res.append(0)
    elif c == "B":
      res.append(1)
    elif c == "C":
      res.append(2)
  return res

def get_alpha(x):
  return "ABC"[x]

for i in range(N):
  ind_x,ind_y = get_ind(S[i])
  if val[ind_x] == 0 and val[ind_y] == 0:
    print("No")
    return
  if val[ind_x] < val[ind_y]:
    ans += [get_alpha(ind_x)]
    val[ind_x] += 1
    val[ind_y] -= 1
  elif val[ind_x] > val[ind_y]:
    ans += [get_alpha(ind_y)]
    val[ind_y] += 1
    val[ind_x] -= 1
  else:
    if i + 1 < N and get_alpha(ind_x) in S[i + 1]:
      ans += [get_alpha(ind_x)]
      val[ind_x] += 1
      val[ind_y] -= 1
    else:
      ans += [get_alpha(ind_y)]
      val[ind_y] += 1
      val[ind_x] -= 1
      
print("Yes")
for a in ans:
  print(a)

