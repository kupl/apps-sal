import sys, io
_INPUT = """\
2
"""
# sys.stdin = io.StringIO(_INPUT) # 提出時にコメントアウト
def main():
    n = int(input())
    ng = n + 1
    ok = 1
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if mid * (mid + 1) // 2 <= n + 1:
            ok = mid
        else:
            ng = mid
    ans = n - ok + 1
    print(ans)
def __starting_point():
    main()
__starting_point()
