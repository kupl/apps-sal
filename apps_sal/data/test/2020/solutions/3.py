n = int(input())
x = [0] * 101
y = [0] * 101
for _ in range(n):
  i, j = map(int, input().split())
  x[i] = 1
  y[j] = 1
print(min(sum(x), sum(y)))
