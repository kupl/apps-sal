from itertools import accumulate
N = int(input())
A = list(map(int, input().split()))
P = list(accumulate(A))
l, right = 0, 2
diff = float('inf')
for c in range(1, N - 1):
    p = P[l]
    q = P[c] - P[l]
    while True:
        if abs(p + 2 * A[l + 1] - q) >= abs(p - q):
            break
        p = P[l + 1]
        q = P[c] - P[l + 1]
        l += 1
    r = P[right] - P[c]
    s = P[-1] - P[right]
    while True:
        if abs(r + 2 * A[right + 1] - s) >= abs(r - s):
            break
        r = P[right + 1] - P[c]
        s = P[-1] - P[right + 1]
        right += 1
    diff = min(diff, max(p, q, r, s) - min(p, q, r, s))
print(diff)
