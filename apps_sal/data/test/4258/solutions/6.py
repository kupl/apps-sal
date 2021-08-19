(a, b, t) = map(int, input().split())
ans = 0
for i in range(1, t + 1):
    if i % a == 0:
        ans += b
print(ans)
