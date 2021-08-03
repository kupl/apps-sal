n = int(input())
li = list(map(int, input().split()))
pr = 1
gr = 0
for l in li:
    pr = pr * l
    if pr > 10e17:
        gr = 1
        break
if gr == 1:
    if 0 in li:
        print((0))
    else:
        print("-1")
else:
    print(pr)
