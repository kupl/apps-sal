n = int(input())

order = [[int(__) for __ in input().split()] for _ in range(n)]
order.sort(key=lambda x: x[1])

ans = 0
right = -1
for i in order:
    if right < i[0]:
        ans += 1
        right = i[1]
print(ans)
