raw = [int(x) for x in input().split(' ')]
k = raw[1]
instr = input()

letters = []
for l in instr:
    if l not in letters:
        letters.append(l)

letters.sort()

if k <= len(instr):
    for i in range(k - 1, -1, -1):
        if instr[i] != letters[-1]:
            repl = instr[:i] + letters[letters.index(instr[i]) + 1] + (k - i - 1) * letters[0]
            break
else:
    repl = instr + (k - len(instr)) * letters[0]

print(repl)
