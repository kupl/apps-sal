A, B, K = map(int, input().split())

print(max(0, A-K), end=" ")

K = max(0, K-A)
print(max(0, B-K))

