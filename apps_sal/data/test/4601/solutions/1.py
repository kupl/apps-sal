N, K = list(map(int, input().split()))
H = list(map(int, input().split()))
if len(H) <= K:
    print((0))
else:
    print((sum(sorted(H)[:len(H) - K])))
