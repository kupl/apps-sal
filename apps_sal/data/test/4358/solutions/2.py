pnum = int(input())
plist = list()
for pcnt in range(0, pnum, 1):
    plist.append(int(input()))

half = max(plist) // 2
psum = sum(plist) - half
print(psum)
