# ｃは考えなくて良い　A*B = N - c より　A*B < Nと考えればOK
# N%a == 0 のとき
N = int(input())
ans = 0
for a in range(1, N):
    if N % a == 0:
        ans += (N // a - 1)
    else:
        ans += (N // a)
print(ans)
