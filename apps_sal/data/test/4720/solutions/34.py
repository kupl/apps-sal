N = int(input())
lr = [list(map(int,input().split())) for i in range(N)]
ans = 0
for i in lr:
  ans += i[1] -i[0] + 1
print(ans)
