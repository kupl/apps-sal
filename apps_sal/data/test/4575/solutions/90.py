n = int(input())
d, x = map(int, input().split())
a = [int(input()) for _ in range(n)]
c = 0
for i in range(n):
  c += (d - 1) // a[i] + 1
print(x + c)
