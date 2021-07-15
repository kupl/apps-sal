N = int(input())
d = list(map(int, input().split()))
S = [0]
for i in range(N):
  S.append(S[i] + d[i])
ans = 0
for j in range(N):
  ans += d[-j-1] * S[-j-2]
print(ans)
