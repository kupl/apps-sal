t = int(input())
for j in range(t):
    n = int(input())
    ans = []
    s = list(map(int, input().split()))
    for i in range(n):
        if i % 2 == 0:
            ans.append(-s[i + 1])
            ans.append(s[i])
    print(*ans)
