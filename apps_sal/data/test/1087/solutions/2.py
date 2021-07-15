import sys
readline = sys.stdin.readline
MAX_DIGIT = 40

def main():
    N, K = map(int, readline().rstrip().split())
    K_bin = bin(K)[2:].zfill(MAX_DIGIT)
    A = list(map(int, readline().rstrip().split()))
    A = [bin(a)[2:].zfill(MAX_DIGIT) for a in A]
    dp = [[-1] * 2 for _ in range(MAX_DIGIT+1)]
    # dp[i][j=0,1] = f, 上からi桁まで決めて、j=0: 今のところkと一致, j=1: k未満が確定

    dp[0][0] = 0
    mul = 2 ** (MAX_DIGIT - 1)
    for d in range(MAX_DIGIT):
        cnt = len([1 for a in A if a[d] == '1'])  # Aで元々d桁目にビットが立っているものの個数
        gain0 = cnt * mul
        gain1 = (N - cnt) * mul

        # k未満が確定 -> k未満が確定
        if dp[d][1] != -1:
            # d桁目でk未満が確定しているので、d+1桁目では0でも1でも自由に大きい方を選べる
            dp[d+1][1] = max(dp[d+1][1], dp[d][1] + max(gain0, gain1))
        
        # 今のところkと一致 -> k未満が確定
        if dp[d][0] != -1:
            # Kのd桁目が1だったら、Xのd桁目は0にする
            if K_bin[d] == '1':
                dp[d+1][1] = max(dp[d+1][1], dp[d][0] + gain0) 

        # 今のところkと一致 -> 今のところkと一致
        if dp[d][0] != -1:
            # Kのd桁目と合わせる
            if K_bin[d] == '1':
                dp[d+1][0] = max(dp[d+1][0], dp[d][0] + gain1)
            else:
                dp[d+1][0] = max(dp[d+1][0], dp[d][0] + gain0)
        
        mul //= 2
    
    print(max(dp[MAX_DIGIT]))


def __starting_point():
    main()
__starting_point()
