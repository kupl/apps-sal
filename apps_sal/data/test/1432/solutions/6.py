n = int(input())
a = list(map(int, input().split()))

# n=3
# a=[2,2,4]

b = [0] * n
x = [0] * n
bsum = 0
for i in range(0, n - 1, 2):
    bsum += a[i] - a[i + 1]
b[0] = bsum
x[0] = b[0] + a[n - 1]
for i in range(1, n):
    b[i] = a[i - 1] - b[i - 1] - a[(n + i - 2) % n]
    x[i] = b[i] + a[(i + n - 1) % n]

strx = " ".join(str(xi) for xi in x)
print(strx)
