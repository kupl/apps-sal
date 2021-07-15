def chmin(l, i, v):
  if l[i] > v:
    l[i] = v
    return True
  return False

def main():
    N, M = map(int, input().split())
    keys = []
    for i in range(M):
        a, b = map(int, input().split())
        C = map(int, input().split())
        # mask: nビット目が1なら、n番目のカギを開けられる
        mask = 0
        for c in C:
            mask |= 1 << (c-1)
        keys.append((a, mask))
    
    # N 個のカギを選ぶ、選ばないのパターンを考えると、その組み合わせは2^N 通り
    # コスト無限大で初期化
    patterns = 1 << N
    INF = float("inf")
    # dp[i]: iのnビット目が1なら、n番目のカギを開けられて、その開けられるカギの組み合わせでの最安値を示している
    # 例: dp[3]: 1番目と2番目のカギをあけたいときの最安値
    dp = [ INF ] * patterns
    dp[0] = 0

    # 計算量: O(2^N * M) => 最大でも 4096 * 10^3 ~= 10^6
    for a, mask in keys:
        for i in range(patterns):
            chmin(dp, i|mask, dp[i] + a)

    ans = dp[patterns-1]
    print(-1 if ans == INF else ans)

def __starting_point():
    main()
__starting_point()
