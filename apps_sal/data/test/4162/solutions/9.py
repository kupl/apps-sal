from fractions import gcd
N = int(input())
a = list(map(int, input().split()))


def lcm(A):
    x = A[0]
    for i in range(1, len(a)):
        x = x * A[i] // gcd(x, A[i])
    return x


n = lcm(a) - 1
ans = 0
for v in a:
    ans += n % v
print(ans)
