sa = input().split(' ')
sellers = int(sa[0])
money = int(sa[1])
sa3 = []
c = 0
slist = []
for x in range(sellers):
    sa3 = []
    sa2 = input().split(' ')
    for element in sa2:
        sa3.append(int(element))
    sa3.remove(sa3[0])
    mini = min(sa3)
    if money > mini:
        c += 1
        slist.append(x + 1)

string = ''
for element in slist:
    string += str(element)
    string += ' '
print(c)
print(string.strip())
