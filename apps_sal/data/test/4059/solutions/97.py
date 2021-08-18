n = int(input())

count = 0

for i in range(1, n):
    res = (n - 1) // i
    count += res

print(count)
