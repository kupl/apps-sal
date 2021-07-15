import sys
readline = sys.stdin.readline

N,A,B,C = list(map(int,readline().split()))

# 0,0を作ってはいけない
# 基本的には小さいほうに1を足す
# 両方とも1の場合は、次の操作で選ばれるほうに1を足す
# 両方とも次の操作で選ばれるときはどちらに足してもよい

S = [readline().rstrip() for i in range(N)]
ans = []

for i in range(N):
  if S[i] == "AB":
    if A == 0 and B == 0:
      print("No")
      return
    if A < B:
      ans += ["A"]
      A += 1
      B -= 1
    elif A > B:
      ans += ["B"]
      B += 1
      A -= 1
    else:
      if i + 1 < N and "A" in S[i + 1]:
        ans += ["A"]
        A += 1
        B -= 1
      else:
        ans += ["B"]
        B += 1
        A -= 1
  if S[i] == "AC":
    if A == 0 and C == 0:
      print("No")
      return
    if A < C:
      ans += ["A"]
      A += 1
      C -= 1
    elif A > C:
      ans += ["C"]
      C += 1
      A -= 1
    else:
      if i + 1 < N and "A" in S[i + 1]:
        ans += ["A"]
        A += 1
        C -= 1
      else:
        ans += ["C"]
        C += 1
        A -= 1
  if S[i] == "BC":
    if B == 0 and C == 0:
      print("No")
      return
    if B < C:
      ans += ["B"]
      B += 1
      C -= 1
    elif B > C:
      ans += ["C"]
      C += 1
      B -= 1
    else:
      if i + 1 < N and "B" in S[i + 1]:
        ans += ["B"]
        B += 1
        C -= 1
      else:
        ans += ["C"]
        C += 1
        B -= 1
print("Yes")
for a in ans:
  print(a)
      
    
    

  

