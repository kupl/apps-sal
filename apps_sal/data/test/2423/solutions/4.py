from collections import Counter
n = int(input())
C = Counter()
for _ in range(n - 1):
  C.update(list(map(int, input().split())))
print(sum(1 for a, b in list(C.items()) if b == 1)) 

