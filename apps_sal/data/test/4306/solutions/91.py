(A, B, C, D) = map(int, input().split())
X = set([i for i in range(A, B)])
print(sum([1 for i in range(C, D) if i in X]))
