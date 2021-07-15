n, m = list(map(int, input().split()))
S = set(range(1, m+1))

for i in range(n):
    k, *a = list(map(int, input().split()))
    S &= set(a)

print((len(S)))

