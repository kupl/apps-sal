n, d = list(map(int, input().split()))
k = int(input())
anss = []
for kuzn in range(k):
    x, y = list(map(int, input().split()))
    if x - d <= y <= x + d and -x + d <= y <= -x + 2 * n - d:
        anss.append('YES')
    else:
        anss.append('NO')
for ans in anss:
    print(ans)
