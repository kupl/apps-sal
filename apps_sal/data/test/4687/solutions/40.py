N, K = list(map(int, input().split()))

cnt = 0

ls = []

for i in range(N):
    ls.append(list(map(int, input().split())))

ls.sort(key=lambda x: x[0])

for a, b in ls:
    cnt += b
    if cnt >= K:
        break

print(a)

