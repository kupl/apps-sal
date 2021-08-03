# 175 C
X, K, D = list(map(int, input().split()))
div = abs(X) // D
mod = abs(X) % D
if abs(X) > K * D:
    print(abs(X) - K * D)
elif (K - div) % 2 == 0:
    print(mod)
else:
    print(D - mod)
