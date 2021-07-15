"""
sqrt(p**2 + q**2) <= D
"""

# 入力
N, D = map(int, input().split())
X = list()
Y = list()
for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

# 距離
count = 0
for i in range(N):
    distance = X[i]**2 + Y[i]**2
    if distance <= D*D:
        count += 1

# 結果
print(count)    
