N, K, Q = map(int, input().split())
point = [K] * (N + 1)
for _ in range(Q):
  point[int(input())] += 1
[print('Yes' if point[i] - Q > 0 else 'No') for i in range(1, N + 1)]
