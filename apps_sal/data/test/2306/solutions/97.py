# 写経AC
N = int(input())
T = [int(i) for i in input().split()]
V = [int(i) for i in input().split()]

Ts = sum(T)

# Vmax[t]: t秒での最大速度 (0.5秒間隔)
Vmax = [float("inf")] * (Ts * 2 + 1)

ts = 0
for i in range(N):
    for t in range(T[i]):
        t1 = (ts + t) * 2
        t2 = (ts + t) * 2 + 1
        Vmax[t1] = min(Vmax[t1], V[i])
        Vmax[t2] = min(Vmax[t2], V[i])

    # 時間の区切りの部分は閉区間が重なっている
    Vmax[(ts + T[i]) * 2] = min(Vmax[(ts + T[i]) * 2], V[i])

    ts += T[i]

# 0秒とT秒
Vmax[0] = Vmax[Ts * 2] = 0
# 左から右に
for t in range(Ts * 2):
    Vmax[t + 1] = min(Vmax[t + 1], Vmax[t] + 0.5)
# 右から左に
for t in range(Ts * 2 - 1, 0, -1):
    Vmax[t] = min(Vmax[t], Vmax[t + 1] + 0.5)

ans = 0.0
for i in range(Ts * 2):
    # 台形の公式
    ans += (Vmax[i] + Vmax[i + 1]) * 0.5 / 2

print(ans)
