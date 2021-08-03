K = int(input())
A, B = list(map(int, input().split()))


def ans165(K, A, B):
    ans_count = 0
    for i in range(A, B + 1):
        if i % K == 0:
            ans_count += 1
    if ans_count > 0:
        return "OK"
    else:
        return "NG"


print((ans165(K, A, B)))
