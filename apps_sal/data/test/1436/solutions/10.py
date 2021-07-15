n = int(input())
events = input().split()
untreated = 0
officers = 0
for i in range(len(events)):
    events[i]=int(events[i])
    if events[i]==-1:
        if officers>0:
            officers-=1
        else:
            untreated+=1
    else:
        officers+=events[i]
print(untreated)

