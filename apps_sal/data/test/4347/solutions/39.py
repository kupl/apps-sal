a = int(input())
fact = 1
for i in range(1, a):
  fact *= i
print(int(fact / (a/2)))
