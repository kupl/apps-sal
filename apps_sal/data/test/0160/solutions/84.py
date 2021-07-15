def divisors(N):
    return sorted(sum((list({n, N // n}) for n in range(1, int(N ** 0.5) + 1) if not N % n), []), reverse=True)
N, K = map(int, input().split())
A = tuple(map(int, input().split()))
D = divisors(sum(A))
for d in D:
    L = sorted(a % d for a in A)
    if not sum(L):
        print(d)
        break
    left, right = 0, N - 1
    count = 0
    while left < right:
        if L[left] + L[right] <= d:
            next_right = right - (L[right] + L[left] == d)
            next_left = left + 1
            L[right] += L[left]
            count += L[left]
            L[left] = 0
        else:
            next_left = left
            next_right = right - 1
            m = d - L[right]
            count += m
            L[right] += m
            L[left] -= m
        left, right = next_left, next_right
    if count <= K:
        print(d)
        break
