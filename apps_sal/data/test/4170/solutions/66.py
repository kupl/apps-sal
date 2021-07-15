N = int(input())
H = list(map(int, input().split()))

# 前から順に走査し、移動回数を最大値で更新する
ans, tmp = 0, 0
for i in range(N-1):
  if H[i] >= H[i+1]: tmp += 1
  else:
    ans = max(ans, tmp)
    tmp = 0
    
ans = max(ans, tmp)
print(ans)
