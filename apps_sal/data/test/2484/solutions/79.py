import sys


def input():
    return sys.stdin.readline().strip()


MOD = 10 ** 9 + 7
sys.setrecursionlimit(20000000)
INF = float("inf")


def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 初期値
    right, ans, tmp = 0, 0, 0

    # leftは0〜Nまで
    for left in range(N):
        while right < N and tmp ^ A[right] == tmp + A[right]:
            tmp += A[right]
            ans += right - left + 1
            right += 1

        # リストの長さが0になったら、どちらも一つ進める
        if left == right:
            right += 1
        # それ以外の場合はleftを一つ進める(合計値から一番左の値を引いておく)
        else:
            tmp -= A[left]
    print(ans)


def __starting_point():
    main()

__starting_point()
