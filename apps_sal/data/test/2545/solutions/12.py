n = int(input())
ans = []
for _ in range(n):
    (a, b) = map(int, input().split())
    (m, d) = (min(a, b), abs(a - b))
    if (a + b) % 3 == 0 and 2 * b - a >= 0 and (2 * a - b >= 0):
        ans.append('YES')
    else:
        ans.append('NO')
for x in ans:
    print(x)
