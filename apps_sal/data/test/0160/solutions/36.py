N, K = map(int, input().split())
A = list(map(int, input().split()))
S = sum(A)
max_div = int(S**0.5)

# Sの約数を列挙する
small_div = []
large_div = []
for i in range(1, max_div+1):
  if S%i == 0:
    small_div.append(i)
    large_div.append(S//i)

# 約数を降順に並べる
div = large_div + small_div[::-1]

ans = 1
for d in div:
  r = []
  for a in A:
    r.append(a%d)
  
  r.sort()
  # (d-ri)足すか、ri引くか、それぞれ累積和を求めておく
  minus = [0]*(N+1)
  plus = [0]*(N+1)
  for i, ri in enumerate(r, 1):
    minus[i] = minus[i-1] + ri
  
  for i, ri in enumerate(r[::-1], 1):
    plus[i] = plus[i-1] + (d - ri)
  
  plus = plus[::-1]
  for m, p in zip(minus, plus):
    if m == p and m <= K:
      ans = d
      break
  
  else:
    continue
  
  break

print(ans)
