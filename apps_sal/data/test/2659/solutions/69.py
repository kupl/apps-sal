# 下d+1桁目が初めて9でないとする
# [__X__]99999
# [_X++_]99999に勝つ必要がある
# 10^d(X+1)-1 / (S(X) + 9d) <= (10^d(X+2)-1) / (S(X)+9d+1)
# (S(X)+9d+1)/(S(X)+9d) <= (10^d(X+2)-1)/(10^d(X+1)-1)
# 1/(S(X)+9d) <= 10^d / (10^d(X+1)-1) <= 1/X
# X <= S(X)+9d <= 135

def S(n):
  if n < 10:
    return n
  return S(n//10) + n%10
  
li = [] # 候補、とりあえず十分量作る

for d in range(20):
  a = 10**d
  for x in range(200):
    y = (x+1)*a-1
    if y > 0:
      z = S(y)
      li.append((y,z))
    
li = sorted(list(set(li)),reverse=True)

# 右から見ていって、その時点での最小値タイ以下なら採用
answer = []
min_N,min_S = li[0]
for n,s in li[1:]:
  # n/s < min_N/min_S
  if n*min_S <= s*min_N:
    min_N = n
    min_S = s
    answer.append(n)


K = int(input())
answer.sort()
answer = answer[:K]
print(('\n'.join(map(str,answer))))


