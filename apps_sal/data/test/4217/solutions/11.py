(N, M) = map(int, input().split())
S = set(range(1, M + 1))
for _ in range(N):
    l = list(map(int, input().split()))
    l.remove(l[0])
    s = set(l)
    S = S & s
print(len(S))
