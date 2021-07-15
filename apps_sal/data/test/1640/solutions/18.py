m = {}
n = int(input())
l = list(map(int, input().split()))
Sum = 0
ans = 0

for i in range(n):
  ans += i * l[i] - Sum
  if m.__contains__(l[i] - 1) :
    ans -= m[l[i] - 1]
  if m.__contains__(l[i] + 1) :
    ans += m[l[i] + 1]
  if m.__contains__(l[i]) :
    m[l[i]] += 1
  else:
    m[l[i]] = 1
  Sum += l[i]

print(ans)



