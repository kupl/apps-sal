def main(X, N, P):
    ans = None
    min_dis = 1e8
    for i in range(102):
        #print(f"loop {i}")
        if i in P:
            continue
        #print(abs(X - i))
        if abs(X - i) < min_dis:
            ans = i
            min_dis = abs(X - i)
            #print(ans)

    return ans


def __starting_point():
    X, N = list(map(int, input().split()))
    P = list(map(int, input().split()))
    ans = main(X, N, P)
    print(ans)

__starting_point()
