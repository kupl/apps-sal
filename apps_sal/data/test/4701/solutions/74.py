n = int(input())
k = int(input())
i = 1
for _ in range(n):
    i = i + min(i, k)
print(i)
