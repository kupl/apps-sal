from collections import defaultdict
n = input()
likes = defaultdict(int)
maxlikes = 0
idx = 0
for time, photoid in enumerate(input().split()):
    likes[photoid] +=1
    if likes[photoid] > maxlikes:
        maxlikes = likes[photoid]
        idx = photoid
print(idx)

