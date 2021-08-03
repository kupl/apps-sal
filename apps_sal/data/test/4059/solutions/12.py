n = int(input())
sum = 0
for a in range(1, n):
    sum = sum + (n - 1) // a
print(sum)
