S = input()
T = input()
len_T = len(T)
ans_min_change_word = len_T
for i in range(len(S) - len_T + 1):
    tmp_change_word = 0
    for j in range(len_T):
        if S[i + j] != T[j]:
            tmp_change_word += 1
    ans_min_change_word = min(ans_min_change_word, tmp_change_word)
print(ans_min_change_word)  # (๑•ૅㅁ•๑)
