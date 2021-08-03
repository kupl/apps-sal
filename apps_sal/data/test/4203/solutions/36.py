s = input()
cnt_1 = 0
cnt_2 = 0
for i in range(1, len(s)):
    if i != 1 and i != len(s) - 1 and s[i] == "C":
        cnt_2 += 1
    if s[i].islower():
        cnt_1 += 1
if s[0] == "A" and cnt_2 == 1 and cnt_1 == len(s) - 2:
    print("AC")
else:
    print("WA")
