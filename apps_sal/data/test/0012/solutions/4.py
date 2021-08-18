n = int(input())
ks = input().strip()

prev_g_seq_len = 0
cur__g_seq_len = 0
prev_is_s = True

res = 0
for j in ks:
    if j == 'S':
        prev_g_seq_len = cur__g_seq_len
        cur__g_seq_len = 0
    else:
        cur__g_seq_len += 1
    res = max(res, prev_g_seq_len + cur__g_seq_len + 1)

mmm = ks.count('G')
res = min(mmm, res)


print(res)
