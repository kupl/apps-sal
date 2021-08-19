(X, Y, Z, K) = map(int, input().split())
A = sorted(map(int, input().split()), reverse=True)
B = sorted(map(int, input().split()), reverse=True)
C = sorted(map(int, input().split()), reverse=True)
AB = []
for a in A:
    for b in B:
        AB.append(a + b)
AB = sorted(AB, reverse=True)[:K]
ans = []
for ab in AB:
    for c in C:
        ans.append(ab + c)
ans = sorted(ans, reverse=True)[:K]
print(*ans, sep='\n')
