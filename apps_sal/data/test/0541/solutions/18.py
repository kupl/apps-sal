(N, M) = map(int, input().split())
q = [list(map(int, input().split())) for _ in range(M)]
q = sorted(sorted(q, key=lambda x: x[0]), key=lambda x: x[1])
last = 0
cnt = 0
for (a, b) in q:
    if last < a:
        last = b - 1
        cnt += 1
print(cnt)
