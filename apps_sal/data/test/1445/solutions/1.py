n = int(input())
a = [0 for i in range(n)]
b = [0 for i in range(n)]
inp = input().split()
for i in range(n):
    a[i] = int(inp[i])

for i in range(0, (n + 1) // 2):
    if i % 2:
        b[i] = a[i]
        b[n - i - 1] = a[n - i - 1]
    else:
        b[i] = a[n - i - 1]
        b[n - i - 1] = a[i]
    # print(b)

print(" ".join(str(i) for i in b))
