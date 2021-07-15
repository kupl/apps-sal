from math import ceil
n = int(input())
A = list(map(int, input().split()))
e = ceil(sum(A) / 2)
s = 0
i = 0
while s < e:
  s += A[i]
  i += 1
print(i)
