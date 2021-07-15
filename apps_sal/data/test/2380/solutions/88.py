N, M = list(map(int, input().split()))
A = sorted(list(map(int, input().split())))
BC = [list(map(int, input().split())) for _ in range(M)]

# n番目の要素でソートsort
BC = sorted(BC, reverse=True, key=lambda x: x[1])

m = A[0]
D = []
for b, c in BC:
    if c > m:
        _ = [D.append(c) for i in range(b)]
    else:
        continue
    if len(D) > N:
        break

D.append(0)

for i, d in enumerate(D):
    if i >= N:
        break
    if A[i] < d:
        A[i] = d
    else:
        break

print((sum(A)))

