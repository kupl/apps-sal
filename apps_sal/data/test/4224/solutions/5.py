N = int(input())
A = list(map(int, input().split()))
ans = 0
for i in A:
  n = i
  while n % 2 == 0:
    n //= 2
    ans += 1
print(ans)
