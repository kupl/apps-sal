(K, S) = map(int, input().split())
cnt = 0
for x in range(K + 1):
    for y in range(K + 1):
        if 0 <= S - (x + y) <= K:
            cnt += 1
print(cnt)
