(N, M, C) = map(int, input().split())
B = list(map(int, input().split()))
count = 0
for n in range(N):
    A = list(map(int, input().split()))
    culc = list()
    culc.append(C)
    for i in range(M):
        d = B[i] * A[i]
        culc.append(d)
    if sum(culc) > 0:
        count += 1
print(count)
