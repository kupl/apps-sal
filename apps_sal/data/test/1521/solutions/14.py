p, n = tuple(map(int, input().split(' ')))
mods = []
result = -2
finished = False

for i in range(n):
    if finished:
        input()
    else:
        tmp = int(input()) % p
        if tmp in mods:
            result = i
            finished = True
        mods.append(tmp)

print(result + 1)
