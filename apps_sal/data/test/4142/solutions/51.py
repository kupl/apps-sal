S = input()
 
# Sの各文字は'L', 'R', 'U', 'D'のいずれかであることに注意する
# 1,3,...文字目が'L'でなく、偶数文字目が'R'でないとき 'Yes'とする
N = len(S)
ans = 'Yes'
for i in range(N):
  if (i % 2 == 0 and S[i] == 'L') or (i % 2 == 1 and S[i] == 'R'):
    ans = 'No'
    break
    
print(ans)
