n = int(input())
C = list(input())

if "R" not in C:
    print(0)
    return

W = C.count("W")
R = C.count("R")
w = 0
r = R
ans = float('inf')

for c in C:
    if c == "W":
        w += 1
    else:
        r -= 1
    ans = min(ans, max(w, r))
print(ans)
