n = int(input())
l = sorted(list(map(int, input().split())))

ans = 0

for i in range(2 * n):
    if i % 2 == 0:
        ans += l[i]
print(ans)
