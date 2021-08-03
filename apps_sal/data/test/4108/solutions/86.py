s = input()
t = input()
sl = len(s)
ss = ""
used = [False] * 26
cnt = 0
for i in range(sl):
    if used[(ord(s[i]) - 97) % 26]:
        ss += str(used[(ord(s[i]) - 97) % 26])
    else:
        cnt += 1
        ss += str(cnt)
        used[(ord(s[i]) - 97) % 26] = cnt

used = [False] * 26
tt = ""
cnt = 0
for i in range(sl):
    if used[(ord(t[i]) - 97) % 26]:
        tt += str(used[(ord(t[i]) - 97) % 26])
    else:
        cnt += 1
        tt += str(cnt)
        used[(ord(t[i]) - 97) % 26] = cnt

if ss == tt:
    print("Yes")
else:
    print("No")
