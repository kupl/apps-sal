n = int(input())
d, x = map(int, input().split())
ans = 0
for i in range(n):
    a = int(input())
    cnt = 0
    for j in range(100):
        if j*a + 1 <= d:
            cnt += 1
    ans += cnt
print(ans + x)
