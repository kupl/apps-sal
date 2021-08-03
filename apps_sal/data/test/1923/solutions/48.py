n = int(input())
l = sorted(list(map(int, input().split())))
ans = 0
for i in range(0, n * 2, 2):
    ans += l[i]

print(ans)
