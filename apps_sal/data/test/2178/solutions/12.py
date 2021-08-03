n = int(input())
ids = list(map(int, input().split()))
ids.reverse()
seq = list(map(int, input().split()))
used = [0 for i in range(n + 1)]
result = []
for op in seq:
    if used[op]:
        result.append(0)
        continue
    cnt = 0
    while seq:
        cur = ids[-1]
        cnt += 1
        used[cur] = 1
        ids.pop()
        if cur == op:
            break
    result.append(cnt)
print(*result)
