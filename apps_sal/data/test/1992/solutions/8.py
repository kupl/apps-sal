s = input().split()
n = int(s[0])
m = int(s[1])
k = int(s[2])
s = input().split()
screen = [0 for i in range(n + 1)]
position = [0 for i in range(n + 1)]

sl = 0
a = [[0]]
tg = [0]
for ii in range(n):
    i = ii + 1
    screen[int(s[ii])] = int(i / k) + min(1, i % k)
    tg.append(int(s[ii]))
    sl += 1
    if sl == k or ii == n - 1:
        a.append(tg)
        sl = 0
        tg = [0]
    if i % k == 0:
        position[int(s[ii])] = k
    else:
        position[int(s[ii])] = i % k
s = input().split()
quest = []
for i in range(m):
    quest.append(int(s[i]))
kq = 0

for i in range(m):
    app = quest[i]
    kq += screen[app]
    vt_scr = screen[app]
    vt_pos = position[app]
    if position[app] != 1:
        bef_pos = vt_pos - 1
        bef_scr = vt_scr
        app_bef = a[bef_scr][bef_pos]
        position[app_bef], position[app] = position[app], position[app_bef]
        a[bef_scr][bef_pos], a[vt_scr][vt_pos] = a[vt_scr][vt_pos], a[bef_scr][bef_pos]
    else:
        if screen[app] != 1:
            bef_pos = k
            bef_scr = vt_scr - 1
            app_bef = a[bef_scr][bef_pos]
            position[app_bef], position[app] = position[app], position[app_bef]
            screen[app_bef], screen[app] = screen[app], screen[app_bef]
            a[bef_scr][bef_pos], a[vt_scr][vt_pos] = a[vt_scr][vt_pos], a[bef_scr][bef_pos]
print(kq)
