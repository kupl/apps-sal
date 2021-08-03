a, b, k = map(int, input().split())
[print(i) for i in sorted(set(list(range(a, min(a + k, b + 1))) + list(range(max(a, b - k + 1), b + 1))))]
