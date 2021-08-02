N, K, Q = map(int, input().split())
scores = [K - Q] * N
for _ in range(Q):
    scores[int(input()) - 1] += 1
for score in scores:
    print('Yes' if score > 0 else 'No')
