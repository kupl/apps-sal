n = list(map(int, list(input().strip())))
ans = []
while any(n):
    cur = 0
    for i in range(len(n)):
        cur *= 10
        if n[i]:
            cur += 1
            n[i] -= 1
    ans.append(cur)
print(len(ans))
print(*ans)
