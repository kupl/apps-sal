n,k,M = map(int,input().split())

T = sorted(map(int,input().split()))

sT = sum(T)

def it(p):
  # pタスク完成させるノリ
  score = p*(k+1)
  m = M - p*sT

  if m < 0:
    return 0

  q = n-p

  for t in T:
    if m > q*t:
      m -= q*t
      score += q
    else:
      score += m//t
      break
  return score

print(max(it(i) for i in range(n+1)))
