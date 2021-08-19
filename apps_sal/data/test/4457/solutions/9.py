n = int(input())
s = list(map(lambda x: (int(x[1]), x[0]), enumerate(input().split())))
s.sort(reverse=True)
ans = 0
for i in range(n):
    ans += s[i][0] * i + 1
print(ans)
print(*map(lambda x: x[1] + 1, s))
