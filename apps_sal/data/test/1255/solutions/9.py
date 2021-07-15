n = int(input())
ans = j = 1
prev = []
for i in range(n):
    new = list(map(int, input().split()))
    if new == prev:
        j += 1
    else:
        ans = max(ans, j)
        j = 1
    prev = new
print(max(ans, j))

