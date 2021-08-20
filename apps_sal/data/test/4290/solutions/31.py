(N, M) = map(int, input().split())
cnt = 0
if N >= 2:
    cnt += N * (N - 1) / 2
if M >= 2:
    cnt += M * (M - 1) / 2
print(int(cnt))
