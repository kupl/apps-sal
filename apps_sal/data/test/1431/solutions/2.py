N = int(input())
A = [int(_) for _ in input().split()]

X = [0 for _ in range(N)]
ans = []
for i in range(N)[::-1]:
    v = 0
    for j in range(i, N, i + 1):
        v += X[j]
    if v % 2 != A[i]:
        X[i] = 1
        ans.append(i + 1)

print((len(ans)))
for i in ans:
    print(i)
