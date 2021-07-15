n = int(input())
a = list(map(int,input().split()))
ans = 0
for v in a:
  ans += v-1
print(ans)
