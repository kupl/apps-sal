arr = [0] * 8
for i in range(8):
    arr[i] = input()
(wr, wc, br, bc) = [[], [], [], []]
for i in range(8):
    for j in range(8):
        if arr[i][j] == 'B':
            bc.append(j)
            br.append(i)
        if arr[i][j] == 'W':
            wc.append(j)
            wr.append(i)
bl = len(bc)
wl = len(wc)
wf = 8
bf = 8
for i in range(bl - 1, -1, -1):
    c = bc[i]
    temp = 0
    for j in range(7, -1, -1):
        if arr[j][c] == 'W':
            temp = j
            break
    if temp > br[i]:
        continue
    bf = 7 - br[i]
    break
for i in range(wl):
    c = wc[i]
    temp = 8
    for j in range(8):
        if arr[j][c] == 'B':
            temp = j
            break
    if temp < wr[i]:
        continue
    wf = wr[i]
    break
if bf < wf:
    print('B')
else:
    print('A')
