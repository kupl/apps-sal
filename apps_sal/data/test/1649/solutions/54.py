ls = list(map(int, input().split()))
ls = sorted(ls)
if ls[3] == ls[0] + ls[1] + ls[2] or ls[3] + ls[0] == ls[1] + ls[2]:
    print("Yes")
else:
    print("No")
