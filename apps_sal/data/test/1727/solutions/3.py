a = int(input())
trees = []
for i in range(a):
    trees.append([int(x) for x in input().split()])
trees.append([1000000000000, 1])
left = -10000000000
c = 0
for i in range(a):
    if trees[i][0] - trees[i][1] > left:
        left = trees[i][0]
        c += 1
    elif trees[i][0] + trees[i][1] < trees[i + 1][0]:
        left = trees[i][0] + trees[i][1]
        c += 1
    else:
        left = trees[i][0]
print(c)
