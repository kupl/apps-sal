N, A, B = map(int, input().split(' '))

ans = 0
if (A + B) != 0:
    taple = divmod(N, A + B)
    ans = taple[0] * A
    if B == 0:
        ans = N
    elif taple[1] > A:
        ans += A
    else:
        ans += taple[1]

print(ans)
