T = int(input())
for _ in range(T):
    N = int(input())
    S = list(map(int, input().split()))

    if N % 2 == 1:
        print("Second")
    else:
        S.sort()
        for i in range(0, N, 2):
            if S[i] != S[i + 1]:
                print("First")
                break
        else:
            print("Second")
