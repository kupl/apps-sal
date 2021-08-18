

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0

    for i in range(N):
        tmp = A[i] - B[i]
        if tmp < 0:
            ans += A[i]
            if A[i + 1] < -tmp:
                ans += A[i + 1]
                A[i + 1] = 0
            else:
                ans += -tmp
                A[i + 1] += tmp
        else:
            ans += B[i]

    print(ans)


def __starting_point():
    main()


__starting_point()
