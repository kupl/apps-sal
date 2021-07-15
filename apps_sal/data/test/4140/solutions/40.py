S = input()
checker = '01'*100001
keep1 = checker[:len(S)]
keep2 = checker[1:len(S)+1]
ans_1 = 0
ans_2 = 0
for i in range(len(S)):
    if S[i] != keep1[i]:
        ans_1 += 1
    else:
        ans_2 += 1
print(min(ans_1, ans_2))
