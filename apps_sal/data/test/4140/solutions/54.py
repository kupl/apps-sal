s = input()
S = len(s)
li_0 = []
for i in s:
    li_0.append(int(i))
li = [0, 1] * 10 ** 5
li_1 = []
li_2 = []
cnt1 = 0
cnt2 = 0
for i in range(S):
    li_1.append(li[i])
    li_2.append(li[i + 1])
for i in range(S):
    if li_0[i] == li_1[i]:
        cnt1 += 1
    if li_0[i] == li_2[i]:
        cnt2 += 1
if cnt1 >= cnt2:
    print(S - cnt1)
else:
    print(S - cnt2)
