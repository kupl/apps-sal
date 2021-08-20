n = int(input())
r = n
for i in range(n):
    r += (n - i - 1) * (i + 1)
print(r)
