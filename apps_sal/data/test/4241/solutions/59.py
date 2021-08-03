S = str(input())
T = str(input())
if T in S:
    print((0))
    return
max_char_cnt, substr = 0, ""
for i in range(len(S) - len(T) + 1):
    substr = S[i:i + len(T)]
    same_char_cnt = 0
    for s, t in zip(substr, T):
        if s == t:
            same_char_cnt += 1
    max_char_cnt = max(max_char_cnt, same_char_cnt)
    if len(T) - max_char_cnt == 1:
        break
print((len(T) - max_char_cnt))
