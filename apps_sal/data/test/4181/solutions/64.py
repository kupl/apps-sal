def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]

    ans = 0
    for i in range(len(B)-1, -1, -1):
        m = min(A[i+1], B[i])
        ans += m
        A[i+1] -= m
        B[i] -= m

        m = min(A[i], B[i])
        ans += m
        A[i] -= m
        B[i] -= m

    print(ans)

def __starting_point():
    main()

__starting_point()
