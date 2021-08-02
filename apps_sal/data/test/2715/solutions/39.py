def resolve():
    K = int(input())
    N = 50
    ans = [49 + K // N] * N
    for i in range(K % N):
        ans[i] += 1
    for j in range(K % N, N):
        ans[j] -= K % N
    print(N)
    print(*ans)


if '__main__' == __name__:
    resolve()
