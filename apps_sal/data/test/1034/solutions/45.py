X, Y, Z, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

l = []
for a in A:
    for b in B:
        l.append(a + b)
l = sorted(l, reverse=True)[:K]

ans = []
for c in C:
    for k in l:
        ans.append(c + k)

ans = sorted(ans, reverse=True)
print(*ans[:K], sep="\n")
