N = int(input())
S = []
ans = 0

for i in range(N):
    S.append(str(input()))

S = list(set(S))
name = [0 for i in range(5)]

for j in range(len(S)):
    t = str(S[j])
    if t[0] == "M":
        name[0] += 1
    elif t[0] == "A":
        name[1] += 1
    elif t[0] == "R":
        name[2] += 1
    elif t[0] == "C":
        name[3] += 1
    elif t[0] == "H":
        name[4] += 1

for x in range(5):
    for y in range(5):
        if x == y:
            break
        for z in range(5):
            if x == z or y == z:
                break
            if name[x] * name[y] * name[z] > 0:
                ans += name[x] * name[y] * name[z]

print(ans)
