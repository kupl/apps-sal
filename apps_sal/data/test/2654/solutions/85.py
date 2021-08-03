n = int(input())
a, b = [], []
for i in range(n):
    inp = list(map(int, input().split()))
    a.append(inp[0])
    b.append(inp[1])
a.sort()
b.sort()
am = sum(a[(n - 1) // 2:n // 2 + 1])
bm = sum(b[(n - 1) // 2:n // 2 + 1])
print(bm - am + 1)
