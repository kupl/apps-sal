from sys import stdout

m = int(1e9 + 7)
n = int(input())
a = [0] * n
a[0] = 1
k = 0
for _ in range(n):
    s = input()
    if s == "f":
        k += 1
    elif s == "s":
        for j in range(1, k + 1):
            a[j] = (a[j - 1] + a[j]) % m
print(a[k])
