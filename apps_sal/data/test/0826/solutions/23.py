# 入力を整数に変換して受け取る
import sys
sys.setrecursionlimit(10 ** 6)
# 入力を整数に変換して受け取る
def II(): return int(sys.stdin.readline())
# 入力全てを整数に変換したものの配列を受け取る
def LI(): return list(map(int, sys.stdin.readline().split()))
# 入力の文字列を1文字ずつに分けたものの配列を受け取る
def LC(): return list(input())
# 入力の数字列を1桁ずつに分けたものの配列を受け取る
def IC(): return [int(c) for c in input()]
# 入力全てを整数に変換して1引いたものの配列を受け取る
def LLI(rows_number): return [LI() for _ in range(rows_number)]


N = II()
if(N == 1):
    print(1)
else:
    Big = N + 1
    NG = 0
    OK = Big

    def is_ok(arg):
        # 条件問題ごとに定義
        return ((arg + 2) * (arg + 3)) // 2 >= Big

    def meguru_bisect(ng, ok):
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok
    l = meguru_bisect(NG, OK)
    while(l * (l + 1) // 2 <= Big):
        l += 1
    l -= 1
    print(Big - l)
