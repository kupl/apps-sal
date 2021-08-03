n = int(input())
m = 0
a = 0
r = 0
c = 0
h = 0
for _ in range(n):
    s = str(input())
    if s[0] == "M":
        m += 1
    elif s[0] == "A":
        a += 1
    elif s[0] == "R":
        r += 1
    elif s[0] == "C":
        c += 1
    elif s[0] == "H":
        h += 1

# print(m,a,r,c,h)
ans = m * (a * r + a * c + a * h + r * c + r * h + c * h) + a * (r * c + r * h + c * h) + r * c * h
print(ans)
