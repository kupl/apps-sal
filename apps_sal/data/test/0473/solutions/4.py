s = input()

wh = int(s[0] + s[1])
wm = int(s[3] + s[4])

s = input()

th = int(s[0] + s[1])
tm = int(s[3] + s[4])

tm += th * 60

wm += wh * 60

wm -= tm
if(wm < 0):
    wm = 1440 + wm
ansh = str(wm // 60)
ansm = str(wm % 60)
if(len(ansh) < 2):
    ansh = '0' + ansh
if(len(ansm) < 2):
    ansm = '0' + ansm
print(ansh + ":" + ansm)
