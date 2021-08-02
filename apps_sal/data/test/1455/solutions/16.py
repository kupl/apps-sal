n = int(input())
a = (n + 1) // 2 + (n + 1) % 2
print(a)
lx = 1
ly = 1
for i in range(n):
    if ly < a:
        print(ly, lx)
        ly += 1
    else:
        print(ly, lx)
        lx += 1
