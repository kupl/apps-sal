__author__ = 'asmn'
(n, k) = tuple(map(int, input().split()))
print(-1 if n == k else ' '.join(map(str, list(range(2, n - k + 1)) + [1] + list(range(n - k + 1, n + 1)))))
