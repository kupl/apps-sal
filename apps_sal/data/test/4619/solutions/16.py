import sys
imput = sys.stdin.read
(w, h, n) = map(int, input().split())
t = [list(map(int, input().split())) for i in range(n)]
su = []
st = []
sv = []
sw = []
sux = svy = 0
stx = w
swy = h
for j in range(n):
    if t[j][2] == 1:
        su.append(t[j][0])
        sux = max(su)
    elif t[j][2] == 2:
        st.append(t[j][0])
        stx = min(st)
    elif t[j][2] == 3:
        sv.append(t[j][1])
        svy = max(sv)
    else:
        sw.append(t[j][1])
        swy = min(sw)
if sux - stx >= 0 or svy - swy >= 0:
    print(0)
else:
    print((stx - sux) * (swy - svy))
