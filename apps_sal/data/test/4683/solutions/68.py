N = int(input())
A = list(map(int,input().split()))

# 解説を読んで解いた

# 累積和の計算

sm = [0]
for i in range(N):
  sm.append(sm[i]+A[i])

# 累積和を使った解答
ans = 0
for j in range(N):
  ans += A[j]*(sm[N]-sm[j+1])
  
print(ans % (10**9+7))
