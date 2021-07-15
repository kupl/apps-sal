import fileinput

for line in fileinput.input():
    x = line


countn = 0
counti = 0
counte = 0
countt = 0

for i in range(len(x)):
    if x[i] == 'n':
        countn+=1
    if x[i] == 'i':
        counti+=1
    if x[i] == 'e':
        counte+=1
    if x[i] =='t':
        countt+=1

countn -= 3
counti -= 1
counte -= 3
countt -= 1

total = 0
if countn>=0 and counti >= 0 and counte >= 0 and countt >= 0:
    total +=1

while countn-2>=0 and counti-1>=0 and counte-3 >= 0 and countt - 1 >= 0:
    countn-=2
    counti-=1
    counte-=3
    countt-=1
    total+=1

print(total)
