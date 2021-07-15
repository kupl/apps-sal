k = int(input())
n = 50
a = [i + k // n for i in range(n)]
for i in range(k % n):
    a[i] += n
    for j in range(n):
        if i != j:
            a[j] -= 1
print(n)
print(*a)
