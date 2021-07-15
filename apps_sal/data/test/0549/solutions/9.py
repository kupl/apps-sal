n = int(input())

a, b = -1, -1
for i in range(1, n+1):
    if n % i == 0:
        if i > n//i:
            break
        a, b = i, n//i
print(a, b)

