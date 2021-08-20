(a, b) = map(int, input().split())
ans = 0
for i in range(b - a):
    ans += i + 1
print(ans - b)
