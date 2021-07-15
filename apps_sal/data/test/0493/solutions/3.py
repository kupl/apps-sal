n=int(input())
s=input()
last = ''
lasti = -1
count=0
for i,v in enumerate(s):
    if v == 'R' and lasti == -1:
       count += i
       last = 'R'
       lasti = i
    elif v=='L' and lasti == -1:
        last = 'L'
        lasti = i
    elif last=='L' and v=='R':
        count += i-lasti-1
        last = 'R'
        lasti = i
    elif last == 'R' and v == 'L':
        count += 0 if (i+lasti)%2 > 0  else 1
        last = 'L'
        lasti = i

if last == 'L':
    count += (n-1)-lasti
if lasti == -1:
    count = n
print(count)


