x, y, a, b, c = list(map(int, input().split()))
plst = list(map(int, input().split()))
qlst = list(map(int, input().split()))
rlst = list(map(int, input().split()))
plst.sort()
qlst.sort()
rlst.sort(reverse = True)
inf = 10 ** 20
plst = plst[-x:] + [inf]
qlst = qlst[-y:] + [inf]
r_pos = 0
p_pos = 0
q_pos = 0
while 1:
    if rlst[r_pos] <= plst[p_pos] and rlst[r_pos] <= qlst[q_pos]:
        break
    elif plst[p_pos] < qlst[q_pos]:
        plst[p_pos] = rlst[r_pos]
        p_pos += 1
        r_pos += 1
    else:
        qlst[q_pos] = rlst[r_pos]
        q_pos += 1
        r_pos += 1
    if r_pos == c:
        break
print((sum(plst) + sum(qlst) - inf * 2))

