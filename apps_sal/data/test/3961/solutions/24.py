n = int(input())
mod = 10 ** 9 + 7
a = [int(_) - 1 for _ in input().split()]
b = [0]
for i in range(1, n + 1):
    v = 2 * b[i - 1] + 2 - b[a[i - 1]]
    b.append(v % mod)
print(b[-1])
