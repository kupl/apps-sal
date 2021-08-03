X = int(input())


def prime_judge(N):
    K = 2
    ans = True
    while K * K <= N:
        if N % K == 0:
            ans = False
            break
        else:
            K += 1
    return ans


while True:
    if prime_judge(X):
        print(X)
        break
    else:
        X += 1
