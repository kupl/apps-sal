n, k = list(map(int, input().split()))
k = abs(k)
# a+b=pとする
# pは、K+2から2Nまでの2N-K-1通りある
# N+1以下のあるpについてa, bの決め方はp-1通り
# N+2以上のあるpについてa, bの決め方は2N-p+1通り
###
# c+d=p-Kとする
# p-Kは、2から2N-Kまでの2N-K-1通りある
# N+K+1以下のあるpについてc, dの決め方はp-K-1通り
# N+K+2以上のあるpについてc, dの決め方は2N-p+K+1通り
###
# 以上より、
# p<=N+1について、a,b,c,dの組み合わせは(p-1)(p-K-1)
# N+2<=p<=N+K+1について、組み合わせは(2N-p+1)(p-K-1)
# p>=N+K+2について、組み合わせは(2N-p+1)(2N-p+K+1)
result = 0
for p in range(k + 2, 2 * n + 1):
  if p <= (n + 1):
    result = result + (p - 1) * (p - k - 1)
  elif (n + 2) <= p <= (n + k + 1):
    result = result + (2 * n - p + 1) * (p - k - 1)
  else:
    result = result + (2 * n - p + 1) * (2 * n - p + k + 1)
    
print(result)

