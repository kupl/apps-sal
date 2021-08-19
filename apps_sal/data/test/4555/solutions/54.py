(A, B, K) = map(int, input().split())
flag = True
for i in range(A, A + K):
    print(i)
    if i == B:
        falg = False
        break
if flag:
    if A + (K - 1) < B - (K - 1):
        for i in range(B - (K - 1), B + 1):
            print(i)
            if i == B:
                break
    else:
        for i in range(A + K, B + 1):
            print(i)
            if i == B:
                break
