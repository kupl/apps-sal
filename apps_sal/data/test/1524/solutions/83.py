S = input()
cnt = [0, 0]
c_ind = 0
l_ind = 0
p = 0
res = [0] * len(S)
for i in range(len(S) - 1):
    cnt[p & 1] += 1
    if S[i] == 'L' and S[i + 1] == 'R':
        j = c_ind & 1 ^ l_ind & 1
        res[c_ind] += cnt[j]
        res[c_ind + 1] += cnt[j ^ 1]
        p = 0
        l_ind = i + 1
        cnt = [0, 0]
    else:
        p += 1
        if S[i] == 'R' and S[i + 1] == 'L':
            c_ind = i
if p > 0:
    cnt[p & 1] += 1
    j = c_ind & 1 ^ l_ind & 1
    res[c_ind] += cnt[j]
    res[c_ind + 1] += cnt[j ^ 1]
for i in range(len(S)):
    print(res[i])
