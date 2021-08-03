S = list(input())

# 白から
cnt1 = 0
for i, s in enumerate(S):
    if i % 2 == 0:
        if s != '0':
            cnt1 += 1
    else:
        if s != '1':
            cnt1 += 1

# 黑から
cnt2 = 0
for i, s in enumerate(S):
    if i % 2 == 0:
        if s != '1':
            cnt2 += 1
    else:
        if s != '0':
            cnt2 += 1

print((min(cnt1, cnt2)))
