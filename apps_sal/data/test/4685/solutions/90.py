(A, B, C) = map(int, input().split())
K = int(input())
print(sum([A, B, C]) + max(A, B, C) * 2 ** K - max(A, B, C))
