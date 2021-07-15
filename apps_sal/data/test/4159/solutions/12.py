A, B, K = map(int, input().split())
a = max(0, A-K)
b = max(min(B, A+B-K), 0)
print(a, b)
