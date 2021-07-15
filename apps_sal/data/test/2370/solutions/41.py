from itertools import product
def main(): 
    with open(0) as f:
        N = int(f.readline())
        A = [list(map(int, line.split())) for line in f.readlines()]

    possible = True
    ans = 0
    r = range(N)
    for i,j in product(r, r) :
        if j <= i: continue
        for k in r:
            if k == i or k == j:
                continue
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
