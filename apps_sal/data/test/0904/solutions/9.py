n = int(input())

l = list(map(str, input().split()))
ans = 0
for i in range(len(l)):
  ans = max(ans, sum(map(str.isupper, l[i])))

print(ans)

