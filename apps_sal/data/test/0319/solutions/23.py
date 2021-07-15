t = input().split(" ")
t = [int(e) for e in t]

l = []
for i in range(t[0]):
    tt = input().strip()
    assert len(tt) == t[1]
    l.append(tt)

assert t[0] == len(l)
assert t[1] == len(l[0])

lsum = []
for i in range(t[1]):
    lsum.append(sum(int(l[j][i]) for j in range(t[0])))

for i in range(t[0]):
    can_be_ignore = True

    for j in range(t[1]):
        if lsum[j] == 1 and l[i][j] == '1':
            can_be_ignore = False
            break

    if can_be_ignore:
        print("YES")
        return


print("NO")


