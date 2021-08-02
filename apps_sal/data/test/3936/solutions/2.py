N = int(input())
S1 = list(input())
S2 = list(input())
p = 10**9 + 7
out = 1

if S1[0] == S2[0]:
    out *= 3
    s = 1
    left = "V"
else:
    out *= 3 * 2
    s = 2
    left = "H"

while s < N:
    if S1[s] == S2[s]:
        now = "V"
    else:
        now = "H"
    if left == "V" and now == "V":
        out *= 2
        s += 1
    elif left == "V" and now == "H":
        out *= 2 * 1
        s += 2
    elif left == "H" and now == "V":
        out *= 1
        s += 1
    elif left == "H" and now == "H":
        out *= 3
        s += 2
    out = out % p
    left = now
print(out)
