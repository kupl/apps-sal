n,k = map(int, input().split())
a = [0]*n
for i in range(k):
  c = int(input())
  L = list(map(int, input().split()))
  for l in L:
    a[l-1] = 1
print(a.count(0))
