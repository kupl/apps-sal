3
(n, k) = tuple(map(int, input().split()))
ft = [tuple(map(int, input().split())) for _ in range(n)]
print(max([f - t + k if t > k else f for (f, t) in ft]))
