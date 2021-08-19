(N, M) = map(int, input().split())
ans = set()
for i in range(N):
    A = list(map(int, input().split()))
    a = set(A[1:])
    if not ans:
        ans = a
    else:
        ans = ans & a
print(len(ans))
