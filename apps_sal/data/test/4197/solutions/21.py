n = int(input())
a = list(map(int,input().split()))
b = [0] * n
for i in range(n):
  b[a[i]-1] = i+1
print(*b)
