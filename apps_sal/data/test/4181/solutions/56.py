N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 勇者1...1番目・2番目の街で、B_1体まで
# 勇者2...2番目・3番目の街で、B_2体まで
# 勇者N...N番目・(N+1)番目の街で、B_N体まで

# 1番目の街は1番目の勇者が救う
# 1番目の勇者は1番目の街のモンスターを全力でmin(A_1,B_1) 体倒す
# 残った力で2番目の街のモンスターを全力でmin(A_2,B_1−min(A_1,B_1))体倒す
# 2番目の街に残ったモンスターは2番目の勇者が倒す
# これを繰り返す

ans = sum(A)
for i in range(N):
    if A[i] >= B[i]: A[i] -= B[i]
    else:
        # A[i] < B[i]
        B[i] -= A[i]
        A[i] = 0
        A[i + 1] = max(A[i + 1] - B[i], 0)

# 初めのモンスター数 - 残ったモンスター数 = 勇者たちが倒した数
ans -= sum(A)
print(ans)
