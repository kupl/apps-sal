n = int(input())
c = list(input())
w = 0
r = c.count("R")
ans = r
for i in range(n):
    if c[i] == "W":
        w += 1
    else:
        r -= 1
    if ans > max(w, r):
        ans = max(w, r)

print(ans)
