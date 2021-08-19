(N, M) = map(int, input().split())
L = list(map(int, input().split()))
d = 0
ans = 1
for l in L:
    d += l
    if d <= M:
        ans += 1
    else:
        break
print(ans)
