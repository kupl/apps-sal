l, r = [int(i) for i in input().split()]
for x in range(l, r+1):
    if len(set(str(x))) == len(str(x)):
        print(x)
        break
else:
    print(-1)


