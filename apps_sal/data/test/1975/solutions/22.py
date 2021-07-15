n, m = list(map(int, input().split()))

print(n + m - 1)

for i in range(n):
    print(i + 1, 1)
    
for i in range(1, m):
    print(1, i + 1)

