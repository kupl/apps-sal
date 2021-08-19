k = int(input())
n = 50
print(n)
a = [k // n + 49] * n
for i in range(k % n):
    for j in range(n):
        if i == j:
            a[j] += n
        else:
            a[j] -= 1
print((*a))
