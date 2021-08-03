a, b = input().split()
ans = []
for x in range(1, len(a) + 1):
    for y in range(1, len(b) + 1):
        ans.append(a[:x] + b[:y])
ans = sorted(ans)
print(ans[0])
