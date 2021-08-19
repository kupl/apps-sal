N = int(input())
A = list(map(int, input().split()))
rt = 0
res = 0
x = 0
s = 0
for lt in range(N):
    while rt < N and x ^ A[rt] == s + A[rt]:
        x ^= A[rt]
        s += A[rt]
        rt += 1
    res += rt - lt
    x ^= A[lt]
    s -= A[lt]
print(res)
