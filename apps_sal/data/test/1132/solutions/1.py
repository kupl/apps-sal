bt = 'bus topology'
st = 'star topology'
rt = 'ring topology'
ut = 'unknown topology'


def main():
    (n, m) = list(map(int, input().split()))
    S = [0 for j in range(n)]
    for _ in range(m):
        (x, y) = list(map(int, input().split()))
        S[x - 1] += 1
        S[y - 1] += 1
    if S.count(2) == len(S):
        print(rt)
        return
    elif S.count(2) == len(S) - 2 and S.count(1) == 2:
        print(bt)
        return
    elif S.count(n - 1) == 1 and S.count(1) == len(S) - 1:
        print(st)
        return
    else:
        print(ut)
        return


main()
