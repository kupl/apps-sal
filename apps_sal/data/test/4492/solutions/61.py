def main():
    N, x = list(map(int, input().split()))
    A = list(map(int, input().split()))
    Acount = sum(A)
    if A[0] > x:
        A[0] = x
    for i in range(N-1):
        tmp = A[i] + A[i+1]
        if tmp > x:
            A[i+1] -= tmp - x
    ans = Acount - sum(A)
    print(ans)

def __starting_point():
    main()

__starting_point()
