N, M = map(int, input().split())
H = list(map(int, input().split()))  # 展望台iの標高
assert len(H) == N
paths = [[] for i in range(N)]
for m in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    paths[a].append(b)
    paths[b].append(a)  # 展望台AからBへの道、その逆

count = 0
for a in range(N):
    for b in paths[a]:
        if H[b] >= H[a]:
            break
    else:
        count += 1
print(count)
