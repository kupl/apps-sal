K = int(input())

n = 50
print(n)
a = [i + (K // n) for i in range(n)]

r = K % n
for i in range(n):
    if i < r:
        a[i] = a[i] + n - r + 1
    else:
        a[i] = a[i] - r

print(*a)
