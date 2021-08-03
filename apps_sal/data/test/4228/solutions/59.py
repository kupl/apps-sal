N, L = list(map(int, input().split()))
# L+i-1,i>=1
nin = 10**6
for i in range(N):
    if abs(L + i) < nin:
        nin = abs(L + i)
        nn = L + i

ans = N * (L - 1) + N * (N + 1) * 0.5 - (nn)

print((int(ans)))
