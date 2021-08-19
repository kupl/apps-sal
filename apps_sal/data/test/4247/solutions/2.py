n = int(input())
p = list(map(int, input().split()))
cnt = 0
for i in range(1, n - 1):
    second = p[i]
    scope = sorted([p[i - 1], p[i], p[i + 1]])
    if scope[0] < second and second < scope[2]:
        cnt += 1
print(cnt)
