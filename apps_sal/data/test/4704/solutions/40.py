N = int(input())
a = list(map(int, input().strip().split()))
# 累積和
s_l = []
s = 0

for n in range(N):
    s += a[n]
    s_l.append(s)

MIN = 10**15
for n in range(N - 1):
    MIN = min(MIN, abs(s - s_l[n] * 2))

print(MIN)
