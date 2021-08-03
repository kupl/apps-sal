n = int(input())
x = list(input())
count = n
for i in range(n - 1):
    if x[i] == x[i + 1]:
        count -= 1
print(count)
