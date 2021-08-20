(A, B, K) = list(map(int, input().split()))
if A >= B:
    count = 0
    for i in range(B, 0, -1):
        if A % i == 0 and B % i == 0:
            count += 1
            if count == K:
                print(i)
if B > A:
    count = 0
    for i in range(A, 0, -1):
        if A % i == 0 and B % i == 0:
            count += 1
            if count == K:
                print(i)
