N, X, T = map(int, input().split())

R = 0
# 作った個数
RT = 0
# かかった時間

while R < N:
    R += X
    RT += T

print(RT)
