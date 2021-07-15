N = int(input())
a = [int(b) for b in input().split()]
Alice = 0
Bob = 0

for i in range(1, N+1):
  if i % 2 == 1:
    Alice += a.pop(a.index(max(a)))
  else:
    Bob += a.pop(a.index(max(a)))

print(str(Alice - Bob))
