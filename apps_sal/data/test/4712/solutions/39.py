def inpl(): return list(map(int, input().split()))
H, W = inpl()
ans = [["#"]*(W+2) for _ in range(H+2)]

for h in range(H):
    A = input()
    for w in range(W):
        ans[h+1][w+1] = A[w]

print(*["".join(a) for a in ans], sep="\n")
