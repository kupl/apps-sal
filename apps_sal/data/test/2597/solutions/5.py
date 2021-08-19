K = int(input())
for _ in range(K):
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    for (i, a) in enumerate(A, 1):
        if a < i:
            print(i - 1)
            break
    else:
        print(N)
