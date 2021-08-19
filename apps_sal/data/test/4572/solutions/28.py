import string
S = input()
lst = list(string.ascii_lowercase)
d = {lst[i]: i for i in range(len(lst))}
cnt = [0] * len(lst)
for ch in S:
    cnt[d[ch]] = 1
idx = -1
for i in range(len(cnt)):
    if cnt[i] == 0:
        idx = i
        break
if idx == -1:
    print('None')
else:
    print(lst[idx])
