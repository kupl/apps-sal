n = int(input())
a = list(map(int, input().split()))
b = sum(map(int, input().split()))
c = list(map(int, input().split()))
s = 0
for i in range(n-1):
  if a[i+1] - a[i] == 1:
    s += c[a[i] - 1]
print(b + s)
