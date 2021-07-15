n = int(input())
p = list(map(int,input().split()))

min_num = 10**6
cnt = 0
for i in range(n):
  if p[i] < min_num:
    min_num = p[i]
    cnt += 1
print(cnt)
