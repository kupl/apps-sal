N = int(input())
A = list(map(int, input().split()))


def two_divisor(x):
    cnt = 0
    while x % 2 == 0:
        x //= 2
        cnt += 1
    return cnt


ans = 0
for i in range(N):
    if A[i] % 2 == 0:
        ans += two_divisor(A[i])

print(ans)
