N, K = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort(key=lambda x: x[0])
s = 0
for i in range(N):
    s += lst[i][1]
    if s >= K:
        break
print(lst[i][0])
