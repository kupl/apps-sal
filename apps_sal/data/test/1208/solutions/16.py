n = int(input())

cmax = 0
curr = 0
records = set()

for i in range(n):
    line = input()
    r = int(line[2:])
    if line[0] == '+':
        curr += 1
        cmax = max(curr, cmax)
        records.add(r)
    else:
        if r in records:
            curr -= 1
            records.remove(r)
        else:
            cmax += 1

print(cmax)

