n = int(input())
lis = list(map(int, input().split()))
ans = 0

for i in lis:
  ans += i-1

print(ans)

