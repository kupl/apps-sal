n = int(input())
s = [0] * 5
ans = 0
for i in range(n):
    x = list(input())[0]
    if x == "M":
        s[0] += 1
    if x == "A":
        s[1] += 1
    if x == "R":
        s[2] += 1
    if x == "C":
        s[3] += 1
    if x == "H":
        s[4] += 1

for a in range(5):
    for b in range(a + 1, 5):
        for c in range(b + 1, 5):
            ans += s[a] * s[b] * s[c]

print(ans)
