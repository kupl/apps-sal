n = int(input())
A = list(map(int, input().split()))
cnt = {}
for i in A:
    if i not in cnt:
        cnt[i] = 0
    cnt[i] += 1
mas = 0
z = 0
for u in cnt:
    if mas < cnt[u]:
        mas = cnt[u]
        z = u
print(len(A) - cnt[z])
zind = A.index(z)
for u in range(zind - 1, -1, -1):
    if A[u] < z:
        print(1, u + 1, u + 2)
    elif A[u] > z:
        print(2, 1 + u, u + 2)
for i in range(zind, n):
    if A[i] < z:
        print(1, i + 1, i)
    elif A[i] > z:
        print(2, i + 1, i)
