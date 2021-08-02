n = int(input())
S = list(set([input() for _ in range(n)]))

name = [0] * 5

for s in S:
    if s[0] == "M":
        name[0] += 1
    if s[0] == "A":
        name[1] += 1
    if s[0] == "R":
        name[2] += 1
    if s[0] == "C":
        name[3] += 1
    if s[0] == "H":
        name[4] += 1

ans = 0
for i in range(5):
    for j in range(i + 1, 5):
        for k in range(j + 1, 5):
            ans += name[i] * name[j] * name[k]

print(ans)
