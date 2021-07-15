def main():
    N = int(input())
    r = range(N)
    A = [list(map(int, input().split())) for _ in r]

    for i in r: A[i][i] = float('inf')
    possible = True
    ans = 0
    for i in r :
        for j in range(i+1,N):
            for k in r:
                if A[i][j] < A[i][k] + A[k][j]:
                    continue
                elif A[i][j] == A[i][k] + A[k][j]:
                    break
                else:
                    possible = False
                    break
            else:
                ans += A[i][j]
    print(ans if possible else -1)

def __starting_point():
    main()
__starting_point()
