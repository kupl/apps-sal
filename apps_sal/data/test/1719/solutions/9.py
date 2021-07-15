# 隣接する2文字の入れ替えでAGCとなるパターン(もしくはAGCそのもの)
# AGC
# ACG
# GAC
# AGGC
# ACGC
# ATGC
# AGAC
# AGGC
# AGTC
# 上記を含まない文字列を数える

import sys
readline = sys.stdin.readline

N = int(readline())
DIV = 10 ** 9 + 7

# dp[i][a][b][c] = i文字目について、2つ前がa,1つ前がb,i文字目がdの数で条件を満たすものの数
# 0:"A", 1:"G", 2:"C", 3:"T"
dp = [[[[0] * 4 for b in range(4)] for a in range(4)] for i in range(N)]

C = {0:"A", 1:"G", 2:"C", 3:"T", 4:""}
NG = set(["AGC","ACG","GAC","AGGC","ACGC","AGAC","AGGC","ATGC","AGTC"])

def check_ok(i,j,k,l = 4):
  if (C[i] + C[j] + C[k] + C[l]) in NG:
    return False
  return True

# 3文字目
for i in range(4):
  for j in range(4):
    for k in range(4):
      if check_ok(i,j,k):
        dp[2][i][j][k] += 1

# 4文字目以降を決める
for i in range(2, len(dp) - 1):
  for a in range(4):
    for b in range(4):
      for c in range(4):
        for k in range(4):
          if check_ok(a,b,c,k) and check_ok(b,c,k):
            dp[i + 1][b][c][k] += dp[i][a][b][c]
            dp[i + 1][b][c][k] %= DIV
        
ans = 0
for a in range(4):
  for b in range(4):
    for c in range(4):
      ans += dp[-1][a][b][c]
      ans %= DIV
      
print(ans)
