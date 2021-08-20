l = sorted(list(map(int, input().split())))
ans = 0
for i in range(len(l) - 1):
    ans += l[i + 1] - l[i]
print(ans)
