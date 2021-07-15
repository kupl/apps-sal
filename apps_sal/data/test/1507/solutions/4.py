from sys import stdin, stdout
import string

n,k = list(map(int,stdin.readline().rstrip().split()))
s = list(stdin.readline().rstrip())

doorOpen = {}
doorClosed = {}

for i in range(n):
    if s[i] not in list(doorOpen.keys()):
        doorOpen[s[i]] = i

for i in range(n-1,-1,-1):
    if s[i] not in list(doorClosed.keys()):
        doorClosed[s[i]] = i

events = [(x,'o') for x in list(doorOpen.values())] + [(x,'x') for x in list(doorClosed.values())]

events.sort(key=lambda x: x[1])
events.sort(key = lambda x:x[0])


opened = 0
unguarded = False
for i in range(len(events)):
    if events[i][1]=='o':
        opened+=1
    else:
        opened-=1
    if opened>k:
        unguarded = True
        break

if unguarded:
    print('YES')
else:
    print('NO')
        

