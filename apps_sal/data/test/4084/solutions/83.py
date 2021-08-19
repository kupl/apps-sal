(N, A, B) = map(int, input().split(' '))
ans = 0
if A + B > 0:
    ans = N // (A + B) * A + min(A, N % (A + B))
print(ans)
