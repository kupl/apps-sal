n = list(input())
cnt1 = 0
cnt2 = 0
for i in range(len(n)):
    if i % 2 == 0:
        if n[i] == '0':
            cnt1 += 1
        else:
            cnt2 += 1
    elif n[i] == '1':
        cnt1 += 1
    else:
        cnt2 += 1
print(min(cnt1, cnt2))
