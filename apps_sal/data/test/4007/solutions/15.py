n = int(input())
l = list(map(int, input().strip().split()))
recieved = [False for i in range(n+1)]
recieved[0] = True
for i in range(len(l)):
    recieved[l[i]] = True
recievedNotGiven = []
givenNotRecieved = []
both = []
for i in range(1,n+1):
    if l[i-1] == 0 and recieved[i] == False:
        both.append(i)
    elif l[i-1] == 0:
        recievedNotGiven.append(i)
    elif recieved[i] == False:
        givenNotRecieved.append(i)
if len(both) != 1:
    for i in range(len(recievedNotGiven)):
        l[recievedNotGiven[i]-1] = givenNotRecieved[i]
    for i in range(len(both)):
        if i < len(both)-1:
            l[both[i]-1] = both[i+1]
        else:
            l[both[i]-1] = both[0]
else:
    l[both[0]-1] = givenNotRecieved[0]
    l[recievedNotGiven[0]-1] = both[0]
    for i in range(1,len(givenNotRecieved)):
        l[recievedNotGiven[i]-1] = givenNotRecieved[i]
for i in range(len(l)):
    print(l[i], end = " ")
