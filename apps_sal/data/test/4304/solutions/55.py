a, b = map(int, input().split())
c = b - a
n = 0
for i in range(1, 999+1):
    n += i
    if c == i:
        ans = n - b

print(ans)
