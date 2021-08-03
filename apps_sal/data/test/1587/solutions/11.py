n = int(input())
clist = input()

wcount = clist.count('W')
rcount = n - wcount
aclist = 'R' * rcount + 'W' * wcount

wrcount = 0
rwcount = 0

for i in range(n):
    if clist[i] == aclist[i]:
        continue
    else:
        if clist[i] == 'W':
            wrcount += 1
        else:
            rwcount += 1

print((max(wrcount, rwcount)))
