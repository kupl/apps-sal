n = int(input())

a = list(map(int, input().split()))[::-1]
c = 0
for i in range(1, n):
  if a[i] > a[i-1]:
    c = n-i
    break
print(c)

