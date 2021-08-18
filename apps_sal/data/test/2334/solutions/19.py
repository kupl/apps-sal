import math


def round_school(x):
    i, f = divmod(x, 1)
    return int(i + ((f >= 0.5) if (x > 0) else (f > 0.5)))


line1 = input()
line2 = input()
line3 = input()
addrs = list()
count = int(line1.strip())
for elem in line2.split():
    addrs.append(int(elem))
intline3 = list(map(int, line3.split()))
maxaddr = intline3[0]
fees = intline3[1]
idx = 0
s2 = 0
transactions = 0
val = 0.0
initiallen = len(addrs)
while(idx < initiallen):
    if((addrs[idx] > maxaddr) and (addrs[idx] <= (maxaddr + fees))):
        transactions = transactions + 1
    elif((addrs[idx] > (maxaddr + fees)) and (addrs[idx] <= (2 * maxaddr + fees))):
        transactions = transactions + 1
    elif(addrs[idx] > (2 * maxaddr + fees)):
        mult = int(math.floor(addrs[idx] / (maxaddr + fees)))
        transactions = transactions + mult
        val = addrs[idx] - mult * (maxaddr + fees)
        if(val > maxaddr):
            if(val > (2 + fees)):
                transactions = transactions + 1
    idx = idx + 1

print(transactions * fees)
