t = int(input())
ans = list()
for i in range(t):
    (a, b, c, n) = map(int, input().split())
    d = [a, b, c]
    d.sort()
    if d[2] - d[0] + d[2] - d[1] > n:
        ans.append('NO')
    else:
        n -= d[2] - d[0]
        n -= d[2] - d[1]
        if n % 3 != 0:
            ans.append('NO')
        else:
            ans.append('YES')
print(*ans, sep='\n')
