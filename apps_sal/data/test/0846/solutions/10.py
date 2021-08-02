
n, m = list(map(int, input().split(" ")))

b = list(map(int, input().split(" ")))

a = [-1] * n

for i in b:
    for j in range(i - 1, n):
        if a[j] == -1:
            a[j] = i

print(" ".join(map(str, a)))
