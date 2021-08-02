import sys
readline = sys.stdin.readline


def check(A, B, C, D):
    N = A + B + C + D
    if not (A + C == N // 2 or A + C == -(-N // 2)):
        return False
    even = [2] * C + [0] * A
    odd = [3] * D + [1] * B
    ans = [None] * N
    flag = (B + D == -(-N // 2))
    for i in range(N):
        if (i % 2 == 0) == flag:
            ans[i] = odd[i // 2]
        else:
            ans[i] = even[i // 2]
    if all(abs(a2 - a1) == 1 for a1, a2 in zip(ans, ans[1:])):
        return ans
    return False


A, B, C, D = map(int, readline().split())
ans = check(A, B, C, D)
if ans == False:
    print('NO')
else:
    print('YES')
    print(*ans)
