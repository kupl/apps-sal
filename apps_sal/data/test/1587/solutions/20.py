N = int(input())
c = list(input())
Rn = c.count("R")
Wn = 0
ans = N
for i in range(N + 1):
    if i == 0:
        ans = Rn
    else:
        if c[i - 1] == "R":
            Rn -= 1
        else:
            Wn += 1
        ans = min(ans, min(Rn, Wn) + abs(Rn - Wn))
print(ans)
