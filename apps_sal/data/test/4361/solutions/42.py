(n, k) = map(int, input().split())
h = [int(input()) for _ in range(n)]
h.sort()
ans = [h[i + k - 1] - h[i] for i in range(n - k + 1)]
print(min(ans))
