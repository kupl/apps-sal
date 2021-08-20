(a, b) = map(int, input().split())
ans = 0
for num in range(1, b - a):
    ans += num
print(ans - a)
