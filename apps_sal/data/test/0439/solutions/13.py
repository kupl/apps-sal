n = int(input())
m = int(input())
j = 1
for i in range(n):
    j *= 2
    if j > m:
        break
print(m % j)
