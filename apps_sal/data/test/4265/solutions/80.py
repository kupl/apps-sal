s = input()
t = input()
c = 0
for (i, j) in zip(s, t):
    if i != j:
        c += 1
print(c)
