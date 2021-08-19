RO = input()
ins = input()
n = 0
for x in range(len(ins)):
    if ins[x] == RO[n]:
        n += 1
print(n + 1)
