s = input()

n = len(s)-1
ans = 0
for i in range(2**n):
  t = s[0]
  for j in range(n):
    if i >> j & 1: t += "+" # 該当する場合のみ"+"を追加する
    t += s[j+1] # 次の文字を追加
  ans += eval(t) # 生成した文字列を計算
print(ans)
