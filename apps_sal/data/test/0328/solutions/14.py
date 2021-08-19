n = int(input())
mx = 0
for i in range(n):
    (x, y) = list(map(int, input().split()))
    mx = max(mx, x + y)
print(mx)
