S = input()
T = input()


# 解説を読んで解いた
# Sの何文字目から書き換えるか全探索

ans = [0]*(len(S)-len(T)+1)

for i in range(len(S)-len(T)+1):
  st = S[i:i+len(T)]
  # 一致しない文字の数が書き換える回数になる
  for j in range(len(T)):
    if st[j] != T[j]:
      ans[i] += 1 
      #print(ans)

print(min(ans))
