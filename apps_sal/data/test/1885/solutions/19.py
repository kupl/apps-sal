from math import factorial

n = int(input())
ans = 0
cur = 1
for i in range(7):
    cur *= n - i
ans += cur // factorial(7)
cur = 1
for i in range(6):
    cur *= n - i
ans += cur // factorial(6)
cur = 1
for i in range(5):
    cur *= n - i
ans += cur // factorial(5)
print(ans)
