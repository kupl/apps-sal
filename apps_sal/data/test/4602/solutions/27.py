n = int(input())
k = int(input())
x_l = list(map(int, input().split()))
th = k/2

ans = 0
for x in x_l:
  if x >= th:
    ans += abs(x-k)
  else:
    ans += x
print(ans*2)
