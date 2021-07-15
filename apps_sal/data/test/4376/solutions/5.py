n,m = list(map(int,input().split()))
rooms = [int(i) for i in input().split()]
letters = [int(i) for i in input().split()]

room = rooms[0]
roomsum = 0
cnt = 1
for i in range(m):
    if letters[i]<=room:
        print(cnt,letters[i]-roomsum)
    else:
        while letters[i]>room:
            roomsum = room
            room += rooms[cnt]
            cnt += 1
        print(cnt,letters[i]-roomsum)

