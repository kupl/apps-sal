n, k = list(map(int, input().split()))
r, s, p = list(map(int, input().split()))
t = list(input())

scr = 0
for i in range(k):
    if t[i] == "r":
        scr += p
    elif t[i] == "s":
        scr += r
    elif t[i] == "p":
        scr += s

for i in range(k, n):
    if t[i] == t[i - k]:
        scr += 0
        t[i] = "q"
    else:
        if t[i] == "r":
            scr += p
        elif t[i] == "s":
            scr += r
        elif t[i] == "p":
            scr += s

print(scr)
