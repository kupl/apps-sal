(a, b, c) = list(map(int, input().split()))
K = int(input())
m = max(a, b, c)
print(a + b + c + (2 ** K - 1) * m)
