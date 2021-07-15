n = int(input())
p = list(map(int, input().split()))
count = 0
for i in range(1, n-1):
  p1, p2, p3 = p[i-1], p[i], p[i+1]
  if p1 < p2 < p3 or p3 < p2 < p1:
    count += 1
print(count)
