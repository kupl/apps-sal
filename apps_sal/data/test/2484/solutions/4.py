N = int(input())
A = list(map(int, input().split()))
sums = [0] * (N + 1)
xors = [0] * (N + 1)
for i in range(1, N + 1):
    sums[i] = sums[i - 1] + A[i - 1]
    xors[i] = xors[i - 1] ^ A[i - 1]
ans = 0
for i in range(N):
    l = i
    r = N
    while l + 1 < r:
        m = (l + r) // 2
        if sums[m + 1] - sums[i] == xors[m + 1] ^ xors[i]:
            l = m
        else:
            r = m
    ans += l - i + 1
print(ans)
