n = int(input())
k = int(input())

x = 1
for i in range(n):
    x = min(x * 2, x + k)
print(x)

