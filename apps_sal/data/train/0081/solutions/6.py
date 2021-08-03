T = int(input())
for _ in range(T):
    A = input()
    B = input()
    C = input()
    N = len(A)
    for i in range(N):
        if not (A[i] == C[i] or B[i] == C[i]):
            print("NO")
            break
    else:
        print("YES")
