n = int(input())
max1 = 0
for i in range(n):
    a, b = map(int, input().strip().split())
    d = a + b
    max1 = max(d, max1)
print(max1)
