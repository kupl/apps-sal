n = int(input())
s = input()
t = input()
q = {}
osh = []
rez1 = 0
rez2 = -1
rez3 = -1
for i in range(n):
    if s[i] != t[i]:
        rez1 += 1
        osh.append(i)
        q[t[i]] = i
p = False
sq = False
for i in osh:
    if s[i] in q:
        p = True
        rez2 = i + 1
        f = q[s[i]]
        rez3 = f + 1
        if s[f] == t[i]:
            sq = True
            break
print(rez1 - (2 if sq else 1 if p else 0))
print(rez2, rez3)
