n = int(input())
a =list(map(int, input().split()))
S = 0
for i in range(n):
  S += 1/a[i]
print(1/S)
