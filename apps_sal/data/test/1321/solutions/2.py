n = int(input())
width = 0
height = [0, 0, False]
men = []
for i in range(n):
    man = input().split(' ')
    man[0] = int(man[0])
    man[1] = int(man[1])
    men.append(list(man))
    width += man[0]
    if man[1] > height[0]:
        height[1] = height[0]
        height[0] = man[1]
    elif man[1] == height[0]:
        height[2] = True
    elif man[1] > height[1]:
        height[1] = man[1]
answ = []
for i in range(n):
    answ.append(str((width - men[i][0]) * (height[1] if men[i][1] == height[0] and height[2] == False else height[0])))
print(' '.join(answ))
