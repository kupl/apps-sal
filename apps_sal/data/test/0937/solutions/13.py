def potential(a):
    return a[0] if a[1] == 0 else 0


def theorems(a):
    return a[0] if a[1] == 1 else 0


n, k = list(map(int, input().split()))
A = list(zip(
    list(map(int, input().split())),
    list(map(int, input().split())))
)

awake = 0
for a in A[:k]:
    awake += potential(a)

best = awake
for i, a in enumerate(A[k:]):
    awake += potential(a)
    awake -= potential(A[i])
    if awake > best:
        best = awake

already = sum(
    theorems(a)
    for a in A
)

print(already + best)
