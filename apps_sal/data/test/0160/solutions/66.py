N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
S = sum(A)


def canMake(n):
    B = [a % n for a in A]
    B.sort()

    left = 0
    right = sum(B)
    for i, b in enumerate(B, start=1):
        left += b
        right -= b
        if left == n * (N - i) - right:
            return left <= K
    return False


ans = 1
for i in range(1, int(S**0.5) + 100):
    if S % i != 0:
        continue
    k = S // i

    if canMake(i):
        ans = max(ans, i)
    if canMake(k):
        ans = max(ans, k)
        break

print(ans)
