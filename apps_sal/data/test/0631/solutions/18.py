ans = []
for _ in range(int(input())):
    n, m = map(int, input().split())
    u = list(map(int, input().split()))
    if sum(u) == m:
        ans.append('YES')
    else:
        ans.append('NO')
print(*ans, sep='\n')

