n = int(input())
A = [[int(i) for i in input().split()] for i in range(n)]

ans = 0
for a in A:
    ans = max(ans, sum(a))

print(ans)
