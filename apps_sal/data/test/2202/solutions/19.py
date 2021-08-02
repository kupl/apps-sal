from itertools import accumulate

N, p = list(map(int, input().split()))
A = list(map(int, input().split()))

left = [0] + list(accumulate(A))
right = list(accumulate(A[::-1]))[::-1] + [0]

ans = [(left[i] % p) + (right[i] % p) for i in range(N + 1)]

print(max(ans))
