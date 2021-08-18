H, W = list(map(int, input().split()))
A = []
for _ in range(H):
    a = input()
    if "
    A.append(a)
A_ = ["" for _ in range(len(A))]
for x in range(W):
    f = False
    for a in A:
        if a[x] == "
        f = True
        break
    if f:
        for y, a in enumerate(A):
            A_[y] += a[x]
for a in A_:
    print(a)
