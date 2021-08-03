n = int(input())
cor = 0
satis = True
for i in range(n):
    line = input().split()
    if line[1] == "South":
        cor += int(line[0])
        if cor > 20000:
            satis = False
            break
    elif line[1] == "North":
        cor -= int(line[0])
        if cor < 0:
            satis = False
            break
    else:
        if cor == 20000 or cor == 0:
            satis = False
            break
if cor != 0:
    satis = False
if satis:
    print("YES")
else:
    print("NO")
