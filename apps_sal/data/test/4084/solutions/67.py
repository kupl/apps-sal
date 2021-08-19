(N, A, B) = map(int, input().split(' '))
ans = 0
if A + B > 0:
    taple = divmod(N, A + B)
    ans = taple[0] * A + min(A, taple[1])
print(ans)
