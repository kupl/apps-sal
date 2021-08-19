S = input()
cnt_0 = S.count('0')
min_cnt_01 = min(cnt_0, len(S) - cnt_0)
print(min_cnt_01 * 2)
