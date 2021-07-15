mem = int(input())
array=[]
for i in range(mem):
    str = input()
    array.append([int(x) for x in str.split()])
max_height = 0
weight = 0
for i in array:
    max_height = max(min(i[0],i[1]),max_height)
pl= 10000000000000
for h in range(max_height, 1001):
    weight= 0
    for i in array:
        if i[0] > h:
            weight +=i[0]
        elif i[1] > h:
            weight += i[1]
        else:
            weight += min(i[0], i[1])
    pl = min(pl, weight* h)
print(pl)
