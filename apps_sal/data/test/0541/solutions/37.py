N, M = list(map(int, input().split()))
ans = 0
l = []
for i in range(M):
    a, b = (map(int, input().split()))
    l.append((a, b))
l.sort(key=lambda x: x[1])
cut = -1
for i, j in l:
    if cut >= i:
        continue
    else:
        ans += 1
        cut = j - 1
print(ans)
