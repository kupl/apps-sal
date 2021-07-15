N, M = map(int, input().split())

# 安い店から順に買う
# 安い順にsort => M本に達するまで前から順に買う
A = sorted([list(map(int, input().split())) for _ in range(N)])

num = 0
ans = 0
for i in range(N):
  flag = False
  val = A[i][0]
  max_num = A[i][1]
  for j in range(max_num):
    ans += val
    num += 1
    if num == M:
      flag = True
      break
  if flag: break
    
print(ans)
