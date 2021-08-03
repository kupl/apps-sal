N = int(input())
A = [int(n) for n in input().split()]
ans = [0] * N
for i, v in enumerate(A):
    ans[v - 1] = i + 1

print(' '.join([str(n) for n in ans]))
