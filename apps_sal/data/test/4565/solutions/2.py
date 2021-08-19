n = int(input())
s = input()
W_cnt = [0]
E_cnt = [0]
for ss in s:
    w = W_cnt[-1]
    if ss == 'W':
        w += 1
    W_cnt.append(w)
for ss in reversed(s):
    e = E_cnt[-1]
    if ss == 'E':
        e += 1
    E_cnt.append(e)
E_cnt = E_cnt[::-1]
minc = float('inf')
for i in range(n):
    c = W_cnt[i] + E_cnt[i + 1]
    minc = min(minc, c)
print(minc)
