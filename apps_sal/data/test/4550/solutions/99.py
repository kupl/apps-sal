a, b, c = map(int, input().split())
sortlist = sorted([a, b, c])
if sortlist[0] + sortlist[1] == sortlist[2]:
    print("Yes")
else:
    print("No")
