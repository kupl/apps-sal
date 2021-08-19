n = int(input())
a = []
p = []
prev = 1000000000.0
ans = 0
for i in range(n):
    (x, y) = map(int, input().split())
    if y < prev:
        prev = y
    ans += x * prev
print(ans)
