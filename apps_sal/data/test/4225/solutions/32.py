A, B, C, K = map(int, input().split())

total = 0
if K <= A:
    print(K)
else:
    total += A
    K = K - A
    if K <= B:
        print(total)
    else:
        K = K - B
        if K <= C:
            total -= K
            print(total)
        else:
            total -= C
            print(total)
