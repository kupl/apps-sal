(N, H, M) = map(int, input().split())
st = [H] * (N + 1)
for _ in range(M):
    (l, r, x) = map(int, input().split())
    for i in range(l, r + 1):
        st[i] = min(st[i], x)
print(sum((a ** 2 for a in st[1:])))
