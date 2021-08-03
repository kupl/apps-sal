i = input()
l = len(i)
run = [0] * (l + 1)
for a in range(1, l + 1):
    if i[a - 1] in ['A', 'E', 'I', 'O', 'U', 'Y']:
        run[a] = run[a - 1] + 1
    else:
        run[a] = run[a - 1]
tot = 0

fore = 0
for i in range(1, l + 1):
    fore -= 1 / i

ey = [fore] + [0] * (l)
for i in range(1, l + 1):
    ey[i] = ey[i - 1] + 1 / (l + 1 - i) + 1 / i

for i in range(1, l + 1):
    tot += ey[i] * run[i]
print(tot)
##god = {}
##god2 = {}
# for i in range(0, 15):
##    god[i] = []
##    god2[i] = []
# for i in range(1, l+1):
# for j in range(i, l+1):
# god[j].append("1/"+str(j-i+1))
# god[i-1].append("-1/"+str(j-i+1))
# god2[j].append(1/(j-i+1))
# god2[i-1].append(-1/(j-i+1))
##        tot += (run[j]-run[i-1])/(j-i+1)
# print(tot)
