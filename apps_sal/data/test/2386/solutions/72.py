n = int(input())
aa = list(map(int, input().split()))
am = [aa[i]-(i+1) for i in range(n)]
am = sorted(am)

b1 = am[n//2-1]
b2 = am[n//2]



sum1 = 0
sum2 = 0

for i in range(n):
  sum1 += abs(am[i]-b1)
  sum2 += abs(am[i]-b2)
  

ans = min(sum1, sum2)
print(ans)

