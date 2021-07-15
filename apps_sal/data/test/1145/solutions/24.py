n = int(input())
a = list(map(int, input().split()))
s = sum(a)
a.sort()
for i in range(1, len(a)):
  if a[i-1] >= a[i]:
      a[i] = a[i-1] + 1
print(sum(a) - s)
