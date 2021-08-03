s = input()
cons = 0
ans = [0] * (len(s))
left = 0
right = 0
check1 = True
check2 = False
for i in range(len(s)):
    if check1 == True and s[i] == "L":
        cons = i
        check1 = False
        check2 = True
    if check2 == True and (s[i] == "R" or i == len(s) - 1):
        right = i - 1
        if i == len(s) - 1:
            right += 1
        dum = s[left:right + 1]
        dum_index = dum.index("L")
        dum_len = len(dum)
        div, mod = divmod(dum_len, 2)
        if dum_index % 2 == 0:
            ans[cons] = div + mod
            ans[cons - 1] = div
        else:
            ans[cons] = div
            ans[cons - 1] = div + mod

        check1 = True
        check2 = False
        left = right + 1
print(" ".join(map(str, ans)))
