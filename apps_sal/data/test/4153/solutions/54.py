S = input()
cnt0 = 0
cnt1 = 0
for i in S:
    if i == '0':
        cnt0 += 1
    else:
        cnt1 += 1
print(min(cnt0, cnt1) * 2)
