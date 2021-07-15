A, B, C = [int(i) for i in input().split()]
K = int(input())

m = max(A, B, C)
print((sum([A, B, C]) - m + m * 2 ** K))

