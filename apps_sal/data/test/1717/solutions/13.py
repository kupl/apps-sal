N = int(input())
X = 1
for i in range(2, N + 1):
    if X % i == 0:
        continue
    else:
        X *= i
if X > 10000000000000.0:
    X = X // 20 + 1
else:
    X += 1
print(X)
