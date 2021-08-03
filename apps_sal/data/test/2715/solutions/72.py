def sub(A):
    m = max(A)
    for i in range(len(A)):
        if A[i] == m:
            A[i] -= len(A)
            m = -(10 ** 40)
        else:
            A[i] += 1


def main():
    K = int(input())
    if K == 0:
        return 2, [1, 1]
    if K == 1:
        return 2, [0, 2]
    if K < 50:
        return K, [K] * K
    k = K // 50
    t = [50 + k] * 50
    for _ in range(50 - (K % 50)):
        sub(t)
    return 50, t


N, A = main()
print(N)
print((*A))
