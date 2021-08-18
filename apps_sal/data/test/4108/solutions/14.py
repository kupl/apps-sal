s, t = list(input()), list(input())
sd, td = {}, {}
for sv in s:
    if sv not in sd:
        sd[sv] = 1
    else:
        sd[sv] += 1
for tv in t:
    if tv not in td:
        td[tv] = 1
    else:
        td[tv] += 1
ss, ts = sorted(sd.values()), sorted(td.values())
if ss == ts:
    print("Yes")
else:
    print("No")
