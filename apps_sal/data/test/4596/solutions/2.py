n = int(input())
a = list(map(int, input().split()))
ans = 1000
for i in range(n):
    x = a[i]
    shift = 0
    while x % 2 == 0:
        x = int(x / 2)
        shift += 1
    ans = min(ans, shift)
    if ans == 0:
        break
print(ans)
