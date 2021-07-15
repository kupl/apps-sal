s = input()
s_length = len(s)

keep = '01' * 100000
keep_1 = keep[:s_length]
keep_2 = keep[1:s_length + 1]


ans_1 = 0
ans_2 = 0
for i in range(s_length):
    if s[i] != keep_1[i]:
        ans_1 += 1
    else:
        ans_2 += 1
print((min(ans_1, ans_2)))

