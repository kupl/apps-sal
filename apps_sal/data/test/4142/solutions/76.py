S = input()
N = len(S)

# 1,3,...文字目が'R'でも'U'でも'D'でもない、または、2,4,...文字目が'L'でも'U'でも'D'でもないとき、'No'を出力する
ans = 'Yes'
for i in range(N):
  if (i % 2 == 0 and S[i] != 'R' and S[i] != 'U' and S[i] != 'D') or (i % 2 == 1 and S[i] != 'L' and S[i] != 'U' and S[i] != 'D'):
    ans = 'No'
    break
    
print(ans)
