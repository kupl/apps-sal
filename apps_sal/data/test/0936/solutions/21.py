total = input()
timeline = input().split()

photos = len(set(timeline))

numberOfLikes = dict.fromkeys(timeline, 0)
max = -1
for pic in timeline:
    numberOfLikes[pic]+=1
    if numberOfLikes[pic]>max:
        max = numberOfLikes[pic]
        res = pic
print(res)
