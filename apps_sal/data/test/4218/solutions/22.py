n = int(input())
odd = 0
for i in range(1, n + 1):
    odd += i % 2 != 0
print(odd / n)
