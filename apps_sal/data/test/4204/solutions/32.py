s = str(input())
k = int(input())
len_s = len(s)
cnt_1 = 0
for i in range(len_s):
    if s[i] == '1':
        cnt_1 += 1
    else:
        moji = s[i]
        break
if cnt_1 >= k:
    print(1)
else:
    print(s[i])
