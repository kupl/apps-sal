N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 勇者1...1番目・2番目の街で、B_1体まで
# 勇者2...2番目・3番目の街で、B_2体まで
# 勇者N...N番目・(N+1)番目の街で、B_N体まで

ans = sum(A)
for i in range(N):
    if A[i] >= B[i]:
        A[i] -= B[i]
    else:
        # A[i] < B[i]
        B[i] -= A[i]
        A[i] = 0
        A[i + 1] = max(A[i + 1] - B[i], 0)

ans -= sum(A)
print(ans)
