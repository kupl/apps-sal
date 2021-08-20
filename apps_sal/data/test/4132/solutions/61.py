N = int(input())
A = list(map(int, input().strip().split()))
A.sort()


def gcd(a, b):
    while True:
        r = a % b
        if r == 0:
            break
        a = b
        b = r
    return b


ans = A[0]
for n in range(N):
    ans = gcd(ans, A[n])
print(ans)
