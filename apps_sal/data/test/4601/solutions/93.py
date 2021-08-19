(N, K) = map(int, input().split())
H = list(map(int, input().split()))
if K == 0:
    print(sum(H))
else:
    print(sum(sorted(H)[:-K]))
