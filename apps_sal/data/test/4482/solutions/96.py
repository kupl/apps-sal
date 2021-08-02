# Nの入力受付
N = int(input())
# aの入力受付
aN = list(map(int, input().split()))
# 平均の値を計算
S = 0
A = 0
for i in aN:
    S += i
A = S / N
if A - int(A) < 0.5:
    A = int(A)
else:
    A = int(A) + 1
# Aにすべて書き換えるときのコストを計算
R = 0
for i in aN:
    R += (i - A)**2
print(R)
