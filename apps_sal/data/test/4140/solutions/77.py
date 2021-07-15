S = input()

idx1, idx2 = 0, 1
cnt1, cnt2 = 0, 0
for s in S:
    s = int(s)
    if s != idx1:
        cnt1 += 1
    if s != idx2:
        cnt2 += 1
    idx1, idx2 = abs(idx1-1), abs(idx2-1)

print(min(cnt1, cnt2))
