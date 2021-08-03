s = input()
t = input()

mn = 1001
for i in range(len(s) - len(t) + 1):
    sm = 0
    for j in range(len(t)):
        if s[i + j] != t[j]:
            sm += 1
    if sm < mn:
        mn = sm
print(mn)
