def resolve():
    inf = 10**10 + 1
    N = int(input())
    A = [int(x) for x in input().split(" ")]
    # 一旦 A[i] - i + 1 を計算する。
    for i in range(N):
        A[i] -= i + 1
    A.sort()
    # 中央値を b とする。
    if len(A) % 2:
        b = A[len(A) // 2]
    else:
        center = len(A) // 2
        b = round((A[center] + A[center - 1]) // 2)

    # 答え
    ans = 0
    for i in range(N):
        ans += abs(A[i] - b)
    print(ans)


resolve()
