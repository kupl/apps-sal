N = int(input())
A = list(map(int, input().split()))
A.insert(0, 0)
B = [0] * (N + 1)
for i in range(N, 0, -1):
    j = 1
    cnt = 0
    while i * j <= N:
        cnt += B[i * j]
        j += 1
    flg = cnt % 2
    if A[i] != flg:
        B[i] = 1
print(sum(B))
for (i, b) in enumerate(B):
    if b == 1:
        print(i)
