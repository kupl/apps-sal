N, M = map(int, input().split())
ls = [tuple(map(int, input().split())) for _ in range(M)]
ls.sort(key=lambda x: x[1], reverse=True)
ls.sort(key=lambda x: x[0], reverse=True)
r = N
cnt = 0
for i in range(M):
    a, b = ls[i]
    if b <= r:
        cnt += 1
        r = a
print(cnt)
