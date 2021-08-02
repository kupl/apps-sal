N, K = list(map(int, input().split()))
d = []
A = []
for _ in range(K):
    d.append(int(input()))
    A.append(list(map(int, input().split())))
cnt = [0 for i in range(N)]
for i in range(K):
    for a in A[i]:
        cnt[a - 1] += 1
print((cnt.count(0)))
