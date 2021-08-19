sa = input().split(' ')
subjs = int(sa[0])
# timeper chapter
time = int(sa[1])
sa2 = input().split(' ')
sa3 = []
for item in sa2:
    sa3.append(int(item))

sa3.sort()

tot = 0
for thing in sa3:
    tot += thing * time

    if time != 1:
        time -= 1


print(tot)
