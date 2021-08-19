(n, d) = list(map(int, input().split()))
L = list(map(int, input().split()))
L.sort()
max = -1
for i in range(n):
    for j in range(i, n):
        if L[j] - L[i] <= d:
            if j - i > max:
                max = j - i
print(n - max - 1)
