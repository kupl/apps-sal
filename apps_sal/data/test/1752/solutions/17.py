n = int(input())
children = list(map(int, input().split()))
children.sort()
right = []
left = []
for i in range(len(children)):
    if i % 2 == 0:
        left.append(children[i])
    else:
        right.append(children[i])
left.extend(reversed(right))
for i in left:
    print(i, end=" ")
