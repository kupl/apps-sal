import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))  # 空白あり


N = I()
t = LI()
v = LI()

max_v = [0] * (N + 1)  # 0秒後,t1秒後,t1+t2秒後,…の時点で出せる最大速度
for i in range(N - 1):
    max_v[i + 1] = min(v[i], v[i + 1], max_v[i] + t[i])
for i in range(N - 2, -1, -1):
    max_v[i + 1] = min(max_v[i + 1], v[i], v[i + 1], max_v[i + 2] + t[i + 1])

ans = 0
for i in range(N):
    if t[i] >= (v[i] - max_v[i]) + (v[i] - max_v[i + 1]):
        ans += t[i] * v[i] - (v[i] - max_v[i])**2 / 2 - (v[i] - max_v[i + 1])**2 / 2
    else:
        x = (t[i] + max_v[i] + max_v[i + 1]) / 2
        ans += t[i] * x - (x - max_v[i])**2 / 2 - (x - max_v[i + 1])**2 / 2

print(ans)
