(n, m) = list(map(int, input().split()))
puzzle = list(sorted(list(map(int, input().split()))))
res = 1000000.0
for i in range(m - n + 1):
    res = min(res, puzzle[i + n - 1] - puzzle[i])
if res == 1000000.0:
    print(0)
else:
    print(res)
