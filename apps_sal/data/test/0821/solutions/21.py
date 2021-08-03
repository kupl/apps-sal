s, v1, v2, t1, t2 = map(int, input().split(' '))
firstTime = t1 + s * v1 + t1
secondTime = t2 + s * v2 + t2

if firstTime < secondTime:
    print("First")
elif firstTime == secondTime:
    print("Friendship")
else:
    print("Second")
