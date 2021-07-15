
url = "https://atcoder.jp/contests/abc162/tasks/abc162_d"
import itertools


def main():
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    route = []
    istuka = [0] * (n+1)
    next = 1
    # 同じ街に訪れるまでループ
    for _ in range(k):
        if istuka[next] == 1:
            break
        else:
            istuka[next] = 1
            route.append(next)
        next = a[next - 1]
    if n >= k:
        print(next)
        return
    ans = route[route.index(next):]
    idx = (k - route.index(next)) % len(ans)
    print(ans[idx])



def __starting_point():
    main()
__starting_point()
