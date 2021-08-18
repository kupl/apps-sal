A, B, X = map(int, input().split())
K = 0
while A * 10**K + B * K < X:
    K += 1
print(min((X - B * K) // A, 10**9))
