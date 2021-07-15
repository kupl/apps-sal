n = int(input())
b = list(map(int, input().split()))
b = [b[0]] + b
sum = 0
for i in range(n-1):
  sum += min(b[i], b[i+1])
sum += b[n-1]
print(sum)
