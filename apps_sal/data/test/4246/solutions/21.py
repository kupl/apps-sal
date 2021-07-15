n = input()

n1 = input()

ind = 0
c = 0
for i in n1:
    if i == n[ind]:
        c += 1
    ind += 1

print(c)
