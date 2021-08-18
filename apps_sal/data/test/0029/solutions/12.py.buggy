ticket = input()
q1, q2 = [(int(i), j) for j, i in enumerate(ticket[:3])], [(int(i), j) for j, i in enumerate(ticket[3:])]
p1, p2 = [i for i, j in q1], [i for i, j in q2]

if sum(p1) > sum(p2):
    p1, p2 = p2, p1
    q1, q2 = q2, q1

if sum(p1) == sum(p2):
    print(0)
    return

for i in range(20):
    if 9 - min(p1) > max(p2):
        pos = min(q1)[1]
        p1[pos] = 9
        q1[pos] = (9, pos)
    else:
        pos = max(q2)[1]
        p2[pos] = 0
        q2[pos] = (0, pos)
    if sum(p1) >= sum(p2):
        print(i + 1)
        return
