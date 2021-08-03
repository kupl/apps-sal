N, K = map(int, input().split())
H = sorted(list(map(int, input().split())))

if not N <= K:
    print(sum(H[0:N - K]))
else:
    print(0)
