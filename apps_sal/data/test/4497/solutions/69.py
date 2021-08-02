N = int(input())
ans = []
for i in range(N):
    q = i + 1
    count = 0
    if q == 1:
        continue
    while True:
        if q % 2 != 0:
            break
        q = q // 2
        count += 1
    ans.append(count)

if len(ans) > 0:
    max_count = max(ans)
    print(ans.index(max_count) + 2)
else:
    print(1)
