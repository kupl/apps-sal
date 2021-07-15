# editorial

def main():
    X, Y = list(map(int, input().split()))

    def solve(x, y):
        """手番が勝つか"""
        return not ((X + Y <= 1) or (abs(X - Y) <= 1))

    cond = solve(X, Y)
    print(('Alice' if cond else 'Brown'))


def __starting_point():
    main()

# e,e
# o,e
# o,o
# o,e遷移は今回は関係なかった

# 負け状態
# 0,0
# 0,1
# 1,1
# まとめると
# X+Y<=1
# abs(X-Y)<=1 <-> >1 と交互

# まとめ方
# 偶奇
# 和と差

__starting_point()
