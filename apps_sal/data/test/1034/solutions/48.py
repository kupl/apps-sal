X, Y, Z, K = map(int, input().split())
A = sorted(list(map(int, input().split())), reverse=True)
B = sorted(list(map(int, input().split())), reverse=True)
C = sorted(list(map(int, input().split())), reverse=True)

l = []
for a in A:
    for b in B:
        l.append(a+b)
l = sorted(l, reverse=True)[:K]


ans = []
for c in C:
    for k in l:
        ans.append(c+k)

ans = sorted(ans, reverse=True)
print(*ans[:K], sep="\n")
