N, K = list(map(int, input().split()))
a = [0] * N
for i in range(K):
    d = int(input())
    A = list(map(int, input().split()))
    for l in A:
        a[l - 1] = 1
print((a.count(0)))
