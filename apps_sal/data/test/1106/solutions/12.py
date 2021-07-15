n = int(input())
ai = list(map(int,input().split()))
ai = [0,0] + ai
cnt = []
ans = 0
while n >= 1:
  for i in range(2 ** n,2 ** (n + 1),2):
      ans += abs(ai[i] - ai[i + 1])
      ai[i // 2] += max(ai[i],ai[i + 1])
  n -= 1
print(ans)
