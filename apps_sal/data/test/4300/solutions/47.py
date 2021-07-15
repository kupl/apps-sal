N = int(input())
d = list(map(int, input().split()))
S = [d[0]]
for i in range(N-1):
  S.append(S[i] + d[i+1])
ans = 0
for j in range(N-1):
  ans += d[j+1] * S[j]
print(ans)
