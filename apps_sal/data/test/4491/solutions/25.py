n = int(input())
al = list(list(map(int, input().split())) for _ in range(2))

ans = 0
for i in range(n):
    # print(al[0][:i+1], al[1][i:])
    ans = max(ans, sum(al[0][:i+1]) + sum(al[1][i:]))

print(ans)
