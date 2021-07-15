# C

N = int(input())
B = [10**10] + list(map(int,input().split())) + [10**10]
ans = 0
for i in range(N):
  ans += min(B[i],B[i+1])
print(ans)

