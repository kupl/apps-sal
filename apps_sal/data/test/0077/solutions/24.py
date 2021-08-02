n = int(input())
s = input()
s = s.split()
l = []
o = []
on = []
sum = 0
for i in s:
    te = int(i)
    l.append(te)
    if(te > 0 and te % 2 == 1):
        o.append(te)
    elif(te > 0 and te % 2 == 0):
        sum += te
    elif(te < 0 and te % 2 == 1):
        on.append(te)
o.sort(reverse=True)
on.sort(reverse=True)
ko = 0
for i in on:
    if(i % 2 == 1):
        ko = i
        break

j = 2
sumo = 0
if(len(o) > 0):
    sumo = o[0]
while(j < len(o)):
    sumo += o[j] + o[j - 1]
    j += 2


if(len(o) == 0):
    print(sum + ko)
elif(len(o) % 2 == 1):
    print(sum + sumo)
elif(len(o) % 2 == 0):
    if(len(on) > 0 and ko < 0):
        print(max(sum + sumo, sum + sumo + ko + o[-1]))
    elif(len(on) > 0 and ko == 0):
        print(sum + sumo)
    else:
        print(sum + sumo)
