N, Q = [int(x) for x in input().split(" ")]

s = input()
AinAC = [0]
CinAC = [0]
c = 0
for i in range(len(s) - 1):
    if s[i] == "A" and s[i + 1] == "C":
        CinAC.append(c)
        c += 1
        AinAC.append(c)
    else:
        AinAC.append(c)
        CinAC.append(c)
else:
    AinAC.append(c)
    CinAC.append(c)

ans = []
for i in range(Q):
    l, r = [int(x) for x in input().split(" ")]
    right = min([AinAC[r], CinAC[r]])
    left = max([AinAC[l - 1], CinAC[l - 1]])
    ans.append(str(right - left))

print(("\n".join(ans)))
