import math
instr = input()
space = instr.find(' ')
inint = int(instr[:space])
outint = int(instr[space + 1:])
nowhalf = outint
counts = 0
adds = 0
while True:
    if inint >= nowhalf:
        print(int(inint - nowhalf + counts + adds))
        break
    counts += 1
    pasthalf = nowhalf
    nowhalf = math.ceil(nowhalf / 2)
    if nowhalf * 2 > pasthalf:
        adds += 1
