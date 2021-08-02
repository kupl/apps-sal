n = list(reversed(input()))

outs = [0] * 9

for i in range(len(n)):
    for x in range(int(n[i])):
        outs[x] += 10**i

outs = list([_f for _f in outs if _f])
print(len(outs))
print(*outs)
