n = int(input())
s = input()

lsum = lcount = rsum = rcount = 0
for ch in s[:n//2]:
    if ch == '?':
        lcount += 1
    else:
        lsum += int(ch)

for ch in s[n//2:]:
    if ch == '?':
        rcount += 1
    else:
        rsum += int(ch)

if lcount > rcount:
    delta = rsum - lsum
    count = lcount - rcount
else:
    delta = lsum - rsum
    count = rcount - lcount
if delta == (count//2)*9:
    print('Bicarp')
else:
    print('Monocarp')
