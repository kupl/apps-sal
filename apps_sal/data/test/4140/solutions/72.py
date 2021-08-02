S = list(input())
ans1 = 0
ans2 = 0
for i in range(len(S)):
    if i % 2 == 0:
        if S[i] == '0':
            ans1 += 1
        else:
            ans2 += 1
    elif i % 2 == 1:
        if S[i] == '0':
            ans2 += 1
        else:
            ans1 += 1
print(min(ans1, ans2))
