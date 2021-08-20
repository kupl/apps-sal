(N, *A) = map(int, open(0).read().split())
C = {}
for a in A:
    if a in C.keys():
        C[a] += 1
    else:
        C[a] = 1
B = list(C.items())
B.sort(key=lambda x: x[0])
ans = 0
for i in range(len(B)):
    count = B[i][1]
    try:
        for j in [-1, 1]:
            if B[i + j][0] == B[i][0] + j:
                count += B[i + j][1]
    except IndexError:
        pass
    ans = max(ans, count)
print(ans)
