import math

n = int(input())
a = list(map(int, input().split()))

lefGcd = [0] * 100100
rigGcd = [0] * 100100

lefGcd[0] = a[0]
rigGcd[n - 1] = a[n - 1]

# 左側からGCDを計算した値を保持する。
for i in range(1, n):
    lefGcd[i] = math.gcd(lefGcd[i - 1], a[i])

# 右側からGCDを計算した値を保持する。
for i in reversed(list(range(0, n - 1))):
    rigGcd[i] = math.gcd(rigGcd[i + 1], a[i])

# 一番左か一番右の値を除去したGCDの値を初期値にする。
ans = max(rigGcd[1], lefGcd[n - 2])

# 左からのGCD,1個飛ばし,右からのGCDを計算し、比較する。
for i in range(1, n - 1):
    ans = max(ans, math.gcd(lefGcd[i - 1], rigGcd[i + 1]))

print(ans)
