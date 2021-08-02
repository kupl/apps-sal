n = int(input())
b = list(map(int, input().split()))
c = b[0] + b[n - 2]
for i in range(n - 2):
    c += min(b[i], b[i + 1])
print(c)
