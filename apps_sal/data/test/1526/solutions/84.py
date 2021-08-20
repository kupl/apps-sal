(a, b, c) = map(int, input().split())
ans = 100000
for i in range(-10, 60):
    cnt = 0
    for x in [a, b, c]:
        while x < i:
            x += 2
            cnt += 1
        cnt += x - i
    ans = min(ans, cnt)
print(ans)
