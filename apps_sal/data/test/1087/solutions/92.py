# bitごとに独立に考えてよい。
# あるビットを反転するかどうか? = ある位に立っているビット数が全体の半数より多いか少ないか?
# K以下と言わず全体の最適なら各bitごとに考えて足しておしまい。
# しかしK以下に限定されている……

# 0以上K以下の整数Xを1個選ぶ
# ある位iのビットが0ならば、スコアに変化なし
# ある位iのビットが1ならば、スコア+=S_i ただしS_iは負の場合もある
# これを繰り返してXに対応するスコアを決める
# スコアの最大値は?
# K以下という成約がなければ、スコアが正のものだけ選べば終了。

# 0~1023のなかなら862 = '0b1101011110' が最高スコア
# だけど上限Kは852なので、10以上減らさねば
# -512, -256, -64, -16, -8-4, -8-2 のうちスコアが高いもの。


n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))

kp1_2 = format(k+1, 'b')
digit_len = len(kp1_2)
sum_nums = sum(nums)

bit_count_dict = {}
for digit in range(digit_len):
    bit_count = 0
    for num in nums:
        if (2 ** digit) & num :
            bit_count += 1
    bit_count_dict[digit] = bit_count

ans = 0
for digit in range(digit_len):
    temp = kp1_2
    ans_candi = sum_nums
    if kp1_2[digit_len-1-digit] == '1':
        # kp1_2[digit]を0にする、それより上位はk+1と同じ、下位は任意なので最適に取れる
        for d_upper in range(digit+1, digit_len):
            if kp1_2[digit_len-1-d_upper] == '1':
                ans_candi += (n - 2 * bit_count_dict[d_upper]) * 2 ** d_upper
        for d_lower in range(0, digit):
            if n - 2 * bit_count_dict[d_lower] > 0:
                ans_candi += (n - 2 * bit_count_dict[d_lower]) * 2 ** d_lower
        
        ans = max(ans, ans_candi)

print(ans)

