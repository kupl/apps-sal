from collections import Counter
T = int(input())
D = {0: 'First', 1: 'Second'}
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    if N % 2 == 1:
        print((D[1]))
    else:
        C = Counter(A)
        # print(C)
        for c in C:
            if C[c] % 2 == 1:
                print((D[0]))
                break
        else:
            print((D[1]))
