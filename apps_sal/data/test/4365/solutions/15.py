K = int(input())
if K % 2 == 0:
    print(int(K * K / 4))
else:
    print(int((K + 1) * (K - 1) / 4))
