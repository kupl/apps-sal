#a = list(map (int,input().split()))
s = str(input())
t = str(input())
box = []
for i in range(len(s) - len(t) + 1):
    a = 0
    for j in range(len(t)):
        if t[j] != s[j + i]:
            a += 1
    box.append(a)
print((min(box)))
