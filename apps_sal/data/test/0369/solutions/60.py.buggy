n, m = map(int, input().split())
s = input()[::-1]
i = 0
ans = []
while i < n:
    for j in range(min(n - i, m), 0, -1):
        if s[i + j] == "0":
            ans.append(j)
            i += j
            break
        if j == 1:
            print(-1)
            return
print(*ans[::-1])
