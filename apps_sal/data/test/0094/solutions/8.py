base = int(input())
num = input()

a = 0
n = ''
l = []
sk = len(str(base))
while num:
    nn = num[-sk:]
    j = 0
    while int(nn) >= base:
        j += 1
        nn = nn[1:]
    while len(nn) > 1 and nn[0] == '0':
        j += 1
        nn = nn[1:]
    l.append(int(nn))
    num = num[:-sk+j]
    
p = 1
for n in l:
    a += p * n
    p *= base
print(a)

