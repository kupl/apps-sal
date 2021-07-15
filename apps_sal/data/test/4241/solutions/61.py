s = list(input())
t = list(input())
d = 0
for a in range(len(s)-len(t)+1):
    c = 0
    for b in range(len(t)):
        if s[a+b] == t[b]:
            c = c + 1
    if c > d:
        d = c
print(len(t)-d)
