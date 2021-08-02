n = int(input())
sectors = list(map(int, input().split()))

ans = 360
for _ in range(n):
    for i in range(n):
        temp = abs(sum(sectors[:i]) - sum(sectors[i:]))
        if temp < ans:
            ans = temp
    sectors[:] = sectors[-1:] + sectors[:-1]
print(ans)
