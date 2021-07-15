n = int(input())
a = list(map(int, input().split()))
prev = 0
S = 0

for i in range(n):
   S += abs(a[i] - prev)
   prev = a[i]

print(S)

