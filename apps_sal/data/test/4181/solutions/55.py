n = int(input())
mons = list(map(int, input().split()))
kill = list(map(int, input().split()))

cnt = 0
for i in range(n - 1, -1, -1):
    if mons[i + 1] < kill[i]:
        cnt += mons[i + 1]
        kill[i] -= mons[i + 1]
        mons[i + 1] = 0
    else:
        cnt += kill[i]
        mons[i + 1] -= kill[i]
        kill[i] = 0
    if mons[i] < kill[i]:
        cnt += mons[i]
        kill[i] -= mons[i]
        mons[i] = 0
    else:
        cnt += kill[i]
        mons[i] -= kill[i]
        kill[i] = 0

print(cnt)
