(a, b) = map(int, input().split())
x = b - a
s = 0
for i in range(1, x, 1):
    s += i
ans = s - a
print(ans)
