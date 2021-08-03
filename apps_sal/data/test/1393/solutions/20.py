s = input()
t = input()
scount = []
tcount = []
yay = 0
whoop = 0
for i in range(130):
    scount.append(0)
    tcount.append(0)
for i in range(len(s)):
    scount[ord(s[i])] += 1
for i in range(len(t)):
    tcount[ord(t[i])] += 1
for i in range(ord('a'), ord('z') + 1):
    lowmin = min(scount[i], tcount[i])
    upmin = min(scount[ord(chr(i).upper())], tcount[ord(chr(i).upper())])
    yay += lowmin + upmin
    scount[i] -= lowmin
    tcount[i] -= lowmin
    scount[ord(chr(i).upper())] -= upmin
    tcount[ord(chr(i).upper())] -= upmin
    whoop += min(scount[i], tcount[ord(chr(i).upper())]) + min(scount[ord(chr(i).upper())], tcount[i])
print(yay, whoop)
